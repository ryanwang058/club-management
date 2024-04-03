from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Max, Min
from .forms import UserUpdateForm, MemberHealthMetricsUpdateForm, FitnessGoalsFormset
from .models import Member, Fitness_Goals, Exercise, Health_Metrics
from datetime import date


@login_required
def manage_profile(request):
  user_form = UserUpdateForm(request.POST or None, instance=request.user)
  health_metrics_form = MemberHealthMetricsUpdateForm(request.POST or None)
  fitness_goals_formset = FitnessGoalsFormset(request.POST or None, queryset=Fitness_Goals.objects.filter(member=request.user.member))

  if request.method == 'POST':
    if user_form.is_valid() and health_metrics_form.is_valid() and fitness_goals_formset.is_valid():
      user_form.save()

      # handles empty entry of health_metrics
      health_metrics_instance = health_metrics_form.save(commit=False)
      health_metrics_instance.member = request.user.member
      health_metrics_instance.date = date.today()  # Sets the date to today
      health_metrics_instance.save()
      # health_metrics_form.save()

      # handles empty entry of fitness goal
      fitness_goals_instances = fitness_goals_formset.save(commit=False)
      for instance in fitness_goals_instances:
        instance.member = request.user.member
        instance.save()
      fitness_goals_formset.save()

      return redirect('/dashboard/member')

  context = {
    'user_form': user_form,
    'health_metrics_form': health_metrics_form,
    'fitness_goals_formset': fitness_goals_formset,
  }

  return render(request, 'manage_profile.html', context)


@login_required
def display_dashboard(request):
  member_id = request.user.member.id  # Assuming Member model is linked to User model
  
  # 1. Exercise Routines
  exercise_routines = Exercise.objects.filter(member_id=member_id).order_by('-date')
  
  # 2. Fitness Achievements
  fitness_goals = Fitness_Goals.objects.filter(member_id=member_id)
  achievements_data = []
  for goal in fitness_goals:
    total_duration = Exercise.objects.filter(member_id=member_id, exercise_type=goal.exercise_type).aggregate(Sum('duration'))['duration__sum'] or 0
    percentage_completed = (total_duration / goal.duration) * 100
    achievements_data.append({
      'exercise_type': goal.exercise_type,
      'total_duration': total_duration,
      'duration_goal': goal.duration,
      'percentage': percentage_completed,
    })
  
  # 3. Health Statistics
  health_metrics = Health_Metrics.objects.filter(member_id=member_id)
  health_statistics = {
    'height': {
      'max': health_metrics.aggregate(Max('height'))['height__max'],
      'max_date': health_metrics.order_by('-height').first().date if health_metrics.exists() else None,
      'min': health_metrics.aggregate(Min('height'))['height__min'],
      'min_date': health_metrics.order_by('height').first().date if health_metrics.exists() else None,
      'current': health_metrics.latest('date').height if health_metrics.exists() else None,
      'current_date': health_metrics.latest('date').date if health_metrics.exists() else None,
    },
    'weight': {
      'max': health_metrics.aggregate(Max('weight'))['weight__max'],
      'max_date': health_metrics.order_by('-weight').first().date if health_metrics.exists() else None,
      'min': health_metrics.aggregate(Min('weight'))['weight__min'],
      'min_date': health_metrics.order_by('weight').first().date if health_metrics.exists() else None,
      'current': health_metrics.latest('date').weight if health_metrics.exists() else None,
      'current_date': health_metrics.latest('date').date if health_metrics.exists() else None,
    },
    'bfp': {
      'max': health_metrics.aggregate(Max('bfp'))['bfp__max'],
      'max_date': health_metrics.order_by('-bfp').first().date if health_metrics.exists() else None,
      'min': health_metrics.aggregate(Min('bfp'))['bfp__min'],
      'min_date': health_metrics.order_by('bfp').first().date if health_metrics.exists() else None,
      'current': health_metrics.latest('date').bfp if health_metrics.exists() else None,
      'current_date': health_metrics.latest('date').date if health_metrics.exists() else None,
    },
  }
  
  context = {
    'exercise_routines': exercise_routines,
    'achievements_data': achievements_data,
    'health_statistics': health_statistics,
  }
  
  return render(request, 'display_dashboard.html', context)

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