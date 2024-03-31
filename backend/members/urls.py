from django.urls import path
from .views import manage_profile 

urlpatterns = [
  path('profile/manage/', manage_profile, name='manage_profile'),
]