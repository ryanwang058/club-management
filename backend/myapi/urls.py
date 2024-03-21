from django.urls import path
from . import views

# define a new URL pattern that maps to the hello_world function in views.py
urlpatterns = [
  path('', views.api_root, name='api_root'),
  path('hello-world/', views.hello_world, name='hello_world'),
]