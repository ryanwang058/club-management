from django.db import models

from members.models import Member
from trainers.models import Trainer
from rooms.models import Room

class Class(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
  duration = models.IntegerField()
  date = models.DateField()

  def __str__(self):
    return f"{self.date} - {self.trainer} with {self.member} in {self.room}"
