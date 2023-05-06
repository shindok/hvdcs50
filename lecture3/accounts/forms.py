from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
        
    class Meta:
        model = CustomUser
        exclude = ['is_active', 'is_admin', 'is_staff', 'date_joined', 'password', 'last_login']
        #TODO: there's a password field being generated somewhere. the db only has a single password.
        # the userCreationForm provides password1 and password2 fields and treat them automatically as passwords
        # without exclude specified for 'password' the there will be charfield input field generated.