import datetime
from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    avg = models.FloatField()
    create_date = models.DateField(default=datetime.datetime.now())