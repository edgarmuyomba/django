from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class signupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'firstname', 'lastname', 'email', 'bio', 'profilePic')