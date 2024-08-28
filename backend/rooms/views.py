from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def manage_room(request):
  context = {}
  return render(request, 'manage_room.html', context)
