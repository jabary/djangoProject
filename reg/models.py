import datetime
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    avg = models.FloatField()
    create_date = models.DateField(default=datetime.datetime.now())
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Course(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    credits = models.IntegerField()
    capacity = models.IntegerField()


class StudentReg(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)



