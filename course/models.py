from django.db import models

class Course(models.Model):
	Name = models.CharField(max_length=200)
	Duration = models.IntegerField(default=3, verbose_name='Duration (in Years)')
	Fees = models.CharField(max_length=50, verbose_name='Fees (Per Semister)')

	def __str__(self):
		return self.Name