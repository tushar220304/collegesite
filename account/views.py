from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, StudentCreateForm, StudentLoginForm, StudentCourseFieldForm
from .models import Myuser, student
from django.contrib.auth.models import User
from datetime import date
import shortuuid

def userpassgen(name, dob):
	password = str(name) + str(dob.day) + str(dob.month) + str(dob.year)
	print('this is a user password : ', password)
	return password

def enrollgen(num):
	today = date.today()
	return '0' + str(num) + '0' + str(today.day) + '0' + str(today.month) + '0' + str(today.year)

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
		course_field = StudentCourseFieldForm(request.POST)
		if form.is_valid() and course_field.is_valid():
			cd = form.cleaned_data
			cf = course_field.cleaned_data
			unique_id = shortuuid.ShortUUID().random(length=5)
			user = User.objects.create_user(
						first_name=cd['first_name'],
						last_name=cd['last_name'],
						email=cd['email'],
						username=cd['first_name'] + cd['last_name'] + unique_id,
						password=userpassgen(cd['first_name'], cd['dob']))
			user.save()
			Myuser(user=user,isStudent=True).save()
			Student = student(enrollmentno=enrollgen(user.id),
							  user=user,
							  Courses=cf['Courses'],
							  phone_no=cd['phone_no'],
							  dob=cd['dob'])
			Student.save()
			return HttpResponse('form is submitted succesfully.')
	else :
		# return HttpResponse('it is a get request')
		form = StudentCreateForm()
		course_field = StudentCourseFieldForm()
		return render(request ,'account/studentcreate.html', {'form': form, 'course_field': course_field})


def stlogin(request):
	if request.method == 'POST':
		form = StudentLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			username = student.objects.get(enrollmentno = cd['enrollmentno']).user.username
			password = cd['password']
			user = authenticate(request, 
									username = username,
									password = password)
			if user is not None:
				if user.is_active:
					if user.myuser.isStudent:
						login(request, user)
						return HttpResponse(f'you are student {user.username}')
					else:
						return HttpResponse('Sorry your are not allowed to login bcoz you are a teacher')
				else:
					return HttpResponse('Disabled Account')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = StudentLoginForm()
		return render(request, 'account/studentlogin.html', {'form': form})