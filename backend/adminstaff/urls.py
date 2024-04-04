from django.urls import path
from .views import process_payment, update_class, monitor_equipment, manage_room

urlpatterns = [
  path('room/manage/', manage_room, name='manage_room'),
  path('equipment/monitor/', monitor_equipment, name='monitor_equipment'),
  path('payment/process/', process_payment, name='process_payment'),
  path('class/update/', update_class, name='update_class')
]