# api endpoints

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Equipment

@api_view(['GET'])
def get_broken_equipment(request):
  broken_equipment = Equipment.objects.filter(status='Broken')
  data = [{"id": eq.id, "equipment_type": eq.equipment_type} for eq in broken_equipment]
  return Response(data)

@api_view(['POST'])
def fix_equipment(request):
  equipment_id = request.data.get('equipment_id')
  try:
    equipment = Equipment.objects.get(id=equipment_id)
    equipment.status = 'Normal'
    equipment.save()
    return Response({"message": "Equipment fixed successfully!"})
  except Equipment.DoesNotExist:
    return Response({"error": "Equipment not found!"}, status=404)