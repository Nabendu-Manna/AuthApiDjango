from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null = True, blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank = True)
    roll = models.IntegerField(blank = True, null = True,)
    city = models.CharField(max_length=20, blank = True)
