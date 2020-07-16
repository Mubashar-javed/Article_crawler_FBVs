from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    # Adding extra email field to UserRegistrationForm.
    email = forms.EmailField()

    class Meta:
        # Telling django what model to use for form creation.
        model = User
        # Informing Django, which fields to use for form
        # The mentioned form will have same fields pattern as same mentioned below.
        
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']
