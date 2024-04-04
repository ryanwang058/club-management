from django.urls import path
from rooms.views import manage_room
from equipment.views import monitor_equipment
from members.views import process_payment
from classes.views import update_class

urlpatterns = [
  path('room/manage/', manage_room, name='manage_room'),
  path('equipment/monitor/', monitor_equipment, name='monitor_equipment'),
  path('payment/process/', process_payment, name='process_payment'),
  path('class/update/', update_class, name='update_class')
]