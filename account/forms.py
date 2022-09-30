from django import forms
from django.contrib.auth.models import User
from .models import Myuser

class LoginForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(widget=forms.PasswordInput)