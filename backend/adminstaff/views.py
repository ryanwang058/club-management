from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from members.models import Payment
from classes.models import Class
from trainers.models import Trainer_Availability
from rooms.models import Room
from equipment.models import Equipment
from .forms import ProcessPaymentForm, UpdateClassForm, ManageRoomForm, MonitorEquipmentForm

@login_required
def process_payment(request):
  if request.method == 'POST':
    form = ProcessPaymentForm(request.POST)
    if form.is_valid():
      payment_id = form.cleaned_data['payment_id']
      payment = Payment.objects.get(id=payment_id)
      payment.status = 'Completed'
      payment.save()
      return redirect(reverse('admin_dashboard'))
  else:
    form = ProcessPaymentForm()

  context = {'form': form}
  return render(request, 'process_payment.html', context)

@login_required
def update_class(request):
  if request.method == 'POST':
    form = UpdateClassForm(request.POST)
    if form.is_valid():
      class_id = form.cleaned_data['class_id']
      selected_class = Class.objects.get(id=class_id)

      trainer_availability = Trainer_Availability.objects.filter(trainer=selected_class.trainer, date=selected_class.date).first()

      if trainer_availability:
        if trainer_availability.status == 'Pending':
          trainer_availability.status = 'Booked'
          trainer_availability.save()
          return redirect(reverse('admin_dashboard'))
        elif trainer_availability.status == 'Booked':
          messages.info(request, 'Already updated Trainer schedule. Please assign a room for this class.')
        else:
          messages.error(request, 'Err: Unknown trainer status')
      else:
        messages.error(request, 'Err: Trainer availability not found')
  else:
    form = UpdateClassForm()

  return render(request, 'update_class.html', {'form': form})

@login_required
def manage_room(request):
  if request.method == 'POST':
    form = ManageRoomForm(request.POST)
    if form.is_valid():
      class_id = form.cleaned_data['class_id']
      room_id = form.cleaned_data['room_id']
      selected_class = Class.objects.get(id=class_id)
      selected_room = Room.objects.get(room_id=room_id)
      
      # Update the selected class with the chosen room
      selected_class.room = selected_room
      selected_class.save()
      
      # Update the room status to 'Booked'
      selected_room.status = 'Booked'
      selected_room.save()
      
      return redirect(reverse('admin_dashboard'))
  else:
    form = ManageRoomForm()

  return render(request, 'manage_room.html', {'form': form})

@login_required
def monitor_equipment(request):
  if request.method == 'POST':
    form = MonitorEquipmentForm(request.POST)
    if form.is_valid():
      equipment_id = form.cleaned_data['equipment_id']
      equipment = Equipment.objects.get(id=equipment_id)
      equipment.status = 'Normal'
      equipment.save()
      return redirect(reverse('admin_dashboard'))
  else:
    form = MonitorEquipmentForm()

  context = {'form': form}
  return render(request, 'monitor_equipment.html', context)