from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, MemberHealthMetricsUpdateForm

@login_required
def manage_profile(request):
  if request.method == 'POST':
    user_form = UserUpdateForm(request.POST, instance=request.user)
    # Check if the user already has health metrics
    if hasattr(request.user.member, 'health_metrics'):
      health_metrics_instance = request.user.member.health_metrics
    else:
      health_metrics_instance = None
    health_metrics_form = MemberHealthMetricsUpdateForm(request.POST, instance=health_metrics_instance)

    if user_form.is_valid() and health_metrics_form.is_valid():
      user_form.save()
      health_metrics = health_metrics_form.save(commit=False)  # Don't save to DB yet
      if health_metrics_instance is None:
        # If there were no health metrics, set the member and save
        health_metrics.member = request.user.member
      health_metrics.save()
      # Redirect to previous page
      return redirect('/dashboard/member')
  else:
    user_form = UserUpdateForm(instance=request.user)
    if hasattr(request.user.member, 'health_metrics'):
      health_metrics_form = MemberHealthMetricsUpdateForm(instance=request.user.member.health_metrics)
    else:
      health_metrics_form = MemberHealthMetricsUpdateForm()

  context = {
    'user_form': user_form,
    'health_metrics_form': health_metrics_form
  }
  return render(request, 'manage_profile.html', context)
