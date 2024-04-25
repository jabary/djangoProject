from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('add/', views.add, name='add'),
    path('form/', views.form, name='form'),
    path('students', views.students)
]
