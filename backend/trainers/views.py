from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TrainerAvailabilityForm

@login_required
def manage_schedule(request):
  trainer = request.user.trainer
  if request.method == 'POST':
    form = TrainerAvailabilityForm(request.POST)
    if form.is_valid():
      availability = form.save(commit=False)
      availability.trainer = trainer
      availability.save()
      # Redirect to the trainer's dashboard
      return redirect('/dashboard/trainer/')
  else:
    form = TrainerAvailabilityForm()

  context = {'form': form}
  return render(request, 'manage_schedule.html', context)
