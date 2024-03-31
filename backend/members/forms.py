from django import forms
from django.contrib.auth import get_user_model
from .models import Member, Health_Metrics

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
