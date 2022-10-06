from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField

class Myuser(models.Model):
	user = models.OneToOneField(User, related_name='myuser', 
								on_delete=models.CASCADE)
	isTeacher = models.BooleanField(default=False)
	isStudent = models.BooleanField(default=False)

	def __str__(self):
		return self.user.first_name

class student(models.Model):
	course_choice = (
		('bca', 'BCA'),
		('bba', 'BBA'),
		('bcom', 'BCom'),
	)
	enrollmentno = models.CharField(unique=True, max_length=100)
	user = models.ForeignKey(User, related_name='student',on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	Courses = models.CharField(choices=course_choice, max_length=200)
	phone_no = models.CharField(max_length=12)
	password = models.CharField(max_length=200)

	def __str__(self):
		return f'Enrollment No - {self.enrollmentno}'