from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, StudentCreateForm
from .models import Myuser

def home(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, 
									username = cd['username'],
									password = cd['password'])
			if user is not None:
				if user.is_active:
					if user.myuser.isTeacher:
						login(request, user)
						return HttpResponse('you are teacher')
					else:
						return HttpResponse('Sorry your are not allowed to login bcoz you are not teacher')
				else:
					return HttpResponse('Disabled Account')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form':form})	

def studentform(request):
	if request.method == 'POST':
		form = StudentCreateForm(request.POST)
		if form.is_valid():
			# cd = form.cleaned_data
			# user = User(first_name=cd['first_name'],
			# 			last_name=cd['last_name'],
			# 			email=cd['email']
			# 			username = f'{first_name + last_name}')
			# user.myuser.isStudent = True
			# user.save()
			# Student = 
		return HttpResponse('form is about to submit')
	else :
		# return HttpResponse('it is a get request')
		form = StudentCreateForm()
		return render(request ,'account/studentcreate.html', {'form': form})