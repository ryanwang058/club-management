# forms.py
from django import forms
from members.models import Payment
from classes.models import Class
from rooms.models import Room
from equipment.models import Equipment

class ProcessPaymentForm(forms.Form):
  payment_id = forms.ChoiceField(choices=[], label="Select Payment to Process")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Populate the choices with pending payments
    pending_payments = Payment.objects.filter(status='Pending').values_list('id', 'amount', 'date', 'member__user__first_name', 'member__user__last_name')
    choices = [(p[0], f"#{p[0]} - {p[3]} {p[4]} - {p[1]} - {p[2]}") for p in pending_payments]
    self.fields['payment_id'].choices = choices

class UpdateClassForm(forms.Form):
  class_id = forms.ChoiceField(choices=[], label="Select Class to update Trainer schedule")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Populate choices with classes that have a null room
    class_choices = Class.objects.filter(room__isnull=True).values_list('id', 'trainer__user__first_name', 'trainer__user__last_name', 'date')
    choices = [(cls[0], f"#{cls[0]}: {cls[1]} {cls[2]} - {cls[3]}") for cls in class_choices]
    self.fields['class_id'].choices = choices

class ManageRoomForm(forms.Form):
  class_id = forms.ChoiceField(choices=[], label="Select Class")
  room_id = forms.ChoiceField(choices=[], label="Select Room")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Populate choices with classes that have a null room
    class_choices = Class.objects.filter(room__isnull=True).values_list('id', 'trainer__user__first_name', 'trainer__user__last_name', 'date')
    self.fields['class_id'].choices = [(cls[0], f"{cls[1]} {cls[2]} - {cls[3]}") for cls in class_choices]
    
    # Populate choices with rooms that are available
    room_choices = Room.objects.filter(status='Available').values_list('room_id', 'room_type')
    self.fields['room_id'].choices = [(room[0], f"#{room[0]} - {room[1]}") for room in room_choices]

class MonitorEquipmentForm(forms.Form):
  equipment_id = forms.ChoiceField(choices=[], label="Select broken Equipment to fix")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Populate the choices with broken equipment
    broken_equipment = Equipment.objects.filter(status='Broken').values_list('id', 'equipment_type')
    choices = [(b[0], f"#{b[0]} - {b[1]}") for b in broken_equipment]
    self.fields['equipment_id'].choices = choices