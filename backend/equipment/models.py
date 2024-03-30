from django.db import models

class Equipment(models.Model):
  equipment_type = models.CharField(max_length=50)
  status = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.equipment_type} - {self.status}"