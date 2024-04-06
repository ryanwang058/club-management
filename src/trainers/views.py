from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TrainerAvailabilityForm
from members.models import Member, Health_Metrics, Fitness_Goals

@login_required
def manage_schedule(request):
  trainer = request.user.trainer
  if request.method == 'POST':
    form = TrainerAvailabilityForm(request.POST)
    if form.is_valid():
      availability = form.save(commit=False)
      availability.trainer = trainer
      availability.save()

      return redirect('/dashboard/trainer/')
  else:
    form = TrainerAvailabilityForm()

  context = {'form': form}
  return render(request, 'manage_schedule.html', context)

@login_required
def view_member(request):
  search_query = request.GET.get('search', None)
  member_profiles = []

  if search_query:
    members = Member.objects.filter(
      user__first_name__icontains=search_query) | Member.objects.filter(user__last_name__icontains=search_query)
  else:
    members = Member.objects.none()  # No search query = no members

  for member in members:
    latest_health_metrics = Health_Metrics.objects.filter(member=member).order_by('-date').first()
    fitness_goals = Fitness_Goals.objects.filter(member=member)
    member_profiles.append({
      'name': f"{member.user.first_name} {member.user.last_name}",
      'email': member.user.email,
      'health_metrics': latest_health_metrics,
      'fitness_goals': fitness_goals,
    })
  
  context = {'member_profiles': member_profiles, 'search_query': search_query}
  return render(request, 'view_member.html', context)