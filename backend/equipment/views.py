from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def monitor_equipment(request):
  context = {}
  return render(request, 'monitor_equipment.html', context)
