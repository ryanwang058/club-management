from django.db import models

# trainers/models.py
from django.db import models

class Trainer(models.Model):
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  exercise_type = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.exercise_type})"


class Trainer_Availability(models.Model):
  trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
  date = models.DateField()
  status = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.trainer.first_name} {self.trainer.last_name} - {self.date} - {self.status}"

