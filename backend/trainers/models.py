from django.db import models
from django.conf import settings

class Trainer(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trainer')
  exercise_type = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.exercise_type})"


class Trainer_Availability(models.Model):
  trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
  date = models.DateField()
  status = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.trainer.first_name} {self.trainer.last_name} - {self.date} - {self.status}"

