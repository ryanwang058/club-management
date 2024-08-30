# api endpoints

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import EquipmentSerializer
from .models import Equipment

# websocket
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class EquipmentViewSet(viewsets.ModelViewSet):
  serializer_class = EquipmentSerializer
  queryset = Equipment.objects.all()

  @action(detail=False, methods=['get'])
  def broken(self, request):
    broken_equipment = Equipment.objects.filter(status='Broken')
    serializer = self.get_serializer(broken_equipment, many=True)

    # Broadcast the updated list of broken equipment
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
      "equipment_updates", 
      {"type": "equipment_update", "message": {"broken_equipment": serializer.data}}
    )
    
    return Response(serializer.data)

  @action(detail=True, methods=['post'])
  def fix(self, request, pk=None):
    try:
      equipment = Equipment.objects.get(pk=pk)
      equipment.status = 'Normal'
      equipment.save()

      # Broadcast the updated equipment status
      channel_layer = get_channel_layer()
      async_to_sync(channel_layer.group_send)(
        "equipment_updates",
        {"type": "equipment_update", "message": {"fixed_equipment_id": pk}}
      )
      
      return Response({"message": "Equipment fixed successfully!"})
    except Equipment.DoesNotExist:
      return Response({"error": "Equipment not found!"}, status=404)