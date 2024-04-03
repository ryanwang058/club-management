from django.urls import path
from .views import manage_schedule
from members.views import view_member

urlpatterns = [
  path('schedule/manage/', manage_schedule, name='manage_schedule'),
  path('view/member/', view_member, name='view_member'),
]