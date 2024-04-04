from django import forms
from django.forms import modelformset_factory
from django.forms.widgets import SelectDateWidget
from django.contrib.auth import get_user_model
from .models import Member, Health_Metrics, Fitness_Goals
from trainers.models import Trainer, Trainer_Availability

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name']

class MemberHealthMetricsUpdateForm(forms.ModelForm):
  class Meta:
    model = Health_Metrics
    fields = ['height', 'weight', 'bfp']

class MemberFitnessGoalsForm(forms.ModelForm):
  class Meta:
    model = Fitness_Goals
    fields = ['exercise_type', 'duration']

# Create a formset for fitness goals, allowing any number of fitness goals to be entered.
FitnessGoalsFormset = modelformset_factory(Fitness_Goals, form=MemberFitnessGoalsForm, extra=1, can_delete=True)


class SearchTrainersForm(forms.Form):
  SESSION_TYPE_CHOICES = [
    ('Strength', 'Personal Training Session - Strength'),
    ('Yoga', 'Group Fitness Class - Yoga'),
    ('Cardio', 'Personal Training Session - Cardio'),
  ]
  session_type = forms.ChoiceField(choices=SESSION_TYPE_CHOICES, label="Select Session Type", required=True)

class BookSessionForm(forms.Form):
  session_number = forms.IntegerField(label="Select a session number", min_value=1)