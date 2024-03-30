from django.db import models

class Member(models.Model):
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Payment(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  payment_type = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateField()
  status = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.member_id} - {self.payment_type} - {self.status}"

class Exercise(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  exercise_type = models.CharField(max_length=50)
  duration = models.IntegerField()  # Duration in minutes
  date = models.DateField()

  def __str__(self):
    return f"{self.member_id} - {self.exercise_type} - {self.date}"

class Health_Metrics(models.Model):
  member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
  height = models.IntegerField()  # height in cm
  weight = models.DecimalField(max_digits=5, decimal_places=2)  # weight in kg
  bfp = models.DecimalField(max_digits=5, decimal_places=2)  # Body Fat Percentage

  def __str__(self):
    return f"{self.member_id} - {self.height}cm - {self.weight}kg"
