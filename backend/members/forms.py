from django import forms
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from .models import Member, Health_Metrics, Fitness_Goals

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