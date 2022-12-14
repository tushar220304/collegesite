from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('student/', views.studentform, name="student"),
    path('studentlogin/', views.stlogin, name='studentlogin'),
]
