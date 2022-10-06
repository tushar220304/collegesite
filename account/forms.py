from django import forms
# from django.contrib.auth.models import User
# from .models import Myuser, student

course_choice = (
		('bca', 'BCA'),
		('bba', 'BBA'),
		('bcom', 'BCom'),
)		

class LoginForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(widget=forms.PasswordInput)

class StudentCreateForm(forms.Form):
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)
	email = forms.EmailField()
	phone_no = forms.CharField()
	course = forms.ChoiceField(choices=course_choice)
	dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
