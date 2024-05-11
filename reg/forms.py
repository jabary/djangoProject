from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Course


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'code', 'credits', 'capacity', 'description']
