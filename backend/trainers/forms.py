from django import forms
from .models import Trainer_Availability

class TrainerAvailabilityForm(forms.ModelForm):
  class Meta:
    model = Trainer_Availability
    fields = ['date', 'status']
    widgets = {
      'status': forms.HiddenInput(),  # Hide status, since it's set automatically to Available
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['status'].initial = 'Available'
