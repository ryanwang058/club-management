from django.db import models
from django.conf import settings

class AdminStaff(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adminstaff')

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
