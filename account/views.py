from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Myuser

# def home(request):

# 	return render('')

def home(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, 
									username = cd['username'],
									password = cd['password'])
			print(user)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated succesfully')
					# Myuser.user = user
					# print(user.isTeacher)
					# print(user.Myuser.isTeacher)
					# if Myuser.isTeacher:
					# 	login(request, user)
					# 	return HttpResponse('you are teacher')
					# else:
					# 	return HttpResponse('Sorry your are not allowed to login bcoz you are not teacher')
				else:
					return HttpResponse('Disabled Account')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form':form})	