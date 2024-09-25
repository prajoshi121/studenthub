from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.createstudent, name='register'),
    path('students/', views.list_students, name='students'),

]