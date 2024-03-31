# views.py in your main app (e.g., club)

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from members.models import Member


def register(request):
  if request.method == 'POST':
    form = MemberRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # Create a Member instance for this user
      Member.objects.create(
        user=user,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
      )
      # Set the is_member flag or add the user to the Members group
      group = Group.objects.get(name='Members') 
      user.groups.add(group)
      user.is_member = True
      user.save()
      # Redirect to the login page or wherever you prefer
      return redirect('login')
  else:
    form = MemberRegistrationForm()
  return render(request, 'registration/register.html', {'form': form})
  
def is_trainer(user):
  return user.groups.filter(name='Trainers').exists() or user.is_superuser

def is_admin_staff(user):
  return user.is_superuser

@login_required
def profile(request):
  return render(request, 'registration/profile.html')

@login_required
@user_passes_test(is_trainer)
def trainer_dashboard(request):
  # Logic for trainer dashboard view
  pass

@login_required
@user_passes_test(is_admin_staff)
def admin_dashboard(request):
  # Logic for admin dashboard view
  pass
