from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def update_class(request):
  context = {}
  return render(request, 'update_class.html', context)
