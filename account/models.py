from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from course.models import  Course
from shortuuid.django_fields import ShortUUIDField
from django.core.exceptions import ValidationError

class Myuser(models.Model):
	user = models.OneToOneField(User, related_name='myuser', 
								on_delete=models.CASCADE)
	isTeacher = models.BooleanField(default=False)
	isStudent = models.BooleanField(default=False)

	def __str__(self):
		return self.user.first_name

	def clean(self):
		if self.isStudent and self.isTeacher:
			raise ValidationError("User cannot be the both student and teacher")

class student(models.Model):
	enrollmentno = models.CharField(unique=True, max_length=100)
	user = models.ForeignKey(User, related_name='student',on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	Courses = models.ForeignKey(Course, related_name='studentenrolled', on_delete=models.CASCADE)
	phone_no = models.CharField(max_length=12)

	def __str__(self):
		return f'Enrollment No - {self.enrollmentno}'