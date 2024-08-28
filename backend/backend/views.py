# views.py in your main app (e.g., backend)

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from members.models import Member, Health_Metrics
from trainers.models import Trainer
from adminstaff.models import AdminStaff
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
  template_name = 'registration/login.html'
  redirect_authenticated_user = True  # Redirect users who are already logged in
  success_url = reverse_lazy('dashboard_dispatcher')


def register(request):
  if request.method == 'POST':
    form = MemberRegistrationForm(request.POST)
    if form.is_valid():
      user_type = form.cleaned_data.get('user_type')
      user = form.save(commit=False)
      if user_type == 'member':
        user.is_member = True
      elif user_type == 'trainer':
        user.is_trainer = True
      else:
        user.is_staff = True
      user.save()
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

@login_required
def member_dashboard(request):
  # Fetch the latest health metrics entry
  latest_health_metrics = Health_Metrics.objects.filter(member=request.user.member).order_by('-date').first()
  context = {
    'latest_health_metrics': latest_health_metrics,
  }
  return render(request, 'dashboard/member.html', context)

@login_required
def trainer_dashboard(request):
  return render(request, 'dashboard/trainer.html')

@login_required
def admin_dashboard(request):
  return render(request, 'dashboard/adminstaff.html')

@login_required
def dashboard_dispatcher(request):
  if request.user.groups.filter(name='Trainers').exists():
    return redirect(reverse_lazy('trainer_dashboard'))
  elif request.user.groups.filter(name='AdminStaff').exists():
    return redirect(reverse_lazy('admin_dashboard'))
  else:
    return redirect(reverse_lazy('member_dashboard'))