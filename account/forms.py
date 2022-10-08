from django import forms
from .models import student

class LoginForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(widget=forms.PasswordInput)

class StudentCourseFieldForm(forms.ModelForm):
	class Meta:
		model = student
		fields = ('Courses',)

class StudentCreateForm(forms.Form):
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)
	email = forms.EmailField()
	phone_no = forms.CharField()
	dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class StudentLoginForm(forms.Form):
	enrollmentno = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
