from django.urls import path
from . import views

# define a new URL pattern that maps to the hello_world function in views.py
urlpatterns = [
  path('hello-world/', views.hello_world, name='hello_world'),
]