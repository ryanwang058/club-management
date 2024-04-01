from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

# Define choices for user types
USER_TYPE_CHOICES = (
  ('member', 'Member'),
  ('trainer', 'Trainer'),
  ('admin_staff', 'Admin Staff'),  # Example, adjust based on your requirements
)

class MemberRegistrationForm(UserCreationForm):
  user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, help_text='Select the type of user.')
  class Meta:
    model = User
    fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

  def clean_user_type(self):
    user_type = self.cleaned_data.get('user_type')
    if not user_type:
      raise ValidationError('User type is required.')
    return user_type

  def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
      user.save()
    return user