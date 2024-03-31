# views.py in your main app (e.g., club)

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from members.models import Member
from trainers.models import Trainer
from adminstaff.models import AdminStaff


def register(request):
  if request.method == 'POST':
    form = MemberRegistrationForm(request.POST)
    if form.is_valid():
      user_type = form.cleaned_data.get('user_type')
      user = form.save()
      if user_type == 'member':
        Member.objects.create(user=user)
        group, _ = Group.objects.get_or_create(name='Members')
      elif user_type == 'trainer':
        Trainer.objects.create(user=user)
        group, _ = Group.objects.get_or_create(name='Trainers')
      else:
        AdminStaff.objects.create(user=user)
        group, _ = Group.objects.get_or_create(name='AdminStaff')
      user.groups.add(group)
      user.save()
     
      # Authenticate and login the user after successful registration
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
      
      # Redirect to a dashboard based on user type
      return redirect('dashboard_dispatcher')
  else:
    form = MemberRegistrationForm()
  return render(request, 'registration/register.html', {'form': form})
  
# def is_trainer(user):
#   return user.groups.filter(name='Trainers').exists()

# def is_admin_staff(user):
#   return user.groups.filter(name='AdminStaff').exists()

@login_required
def member_dashboard(request):
  return render(request, 'dashboard/member.html')

@login_required
# @user_passes_test(is_trainer)
def trainer_dashboard(request):
  return render(request, 'dashboard/trainer.html')

@login_required
# @user_passes_test(is_admin_staff)
def admin_dashboard(request):
  return render(request, 'dashboard/adminstaff.html')

@login_required
def dashboard_dispatcher(request):
  if request.user.groups.filter(name='Trainers').exists():
    return redirect('trainer_dashboard')
  elif request.user.groups.filter(name='AdminStaff').exists():
    return redirect('admin_dashboard')
  else:
    return redirect('member_dashboard')