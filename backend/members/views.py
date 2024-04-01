from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, MemberHealthMetricsUpdateForm, FitnessGoalsFormset
from .models import Fitness_Goals

@login_required
def manage_profile(request):
  user_form = UserUpdateForm(request.POST or None, instance=request.user)
  health_metrics_form = MemberHealthMetricsUpdateForm(request.POST or None, instance=request.user.member.health_metrics if hasattr(request.user.member, 'health_metrics') else None)
  fitness_goals_formset = FitnessGoalsFormset(request.POST or None, queryset=Fitness_Goals.objects.filter(member=request.user.member))

  if request.method == 'POST':
    if user_form.is_valid() and health_metrics_form.is_valid() and fitness_goals_formset.is_valid():
      user_form.save()

      # handles empty entry of health_metrics
      health_metrics_instance = health_metrics_form.save(commit=False)
      health_metrics_instance.member = request.user.member
      health_metrics_instance.save()
      health_metrics_form.save()

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