from django.urls import path
from .views import manage_profile, display_dashboard

urlpatterns = [
  path('profile/manage/', manage_profile, name='manage_profile'),
  path('dashboard/display/', display_dashboard, name='display_dashboard'),
]