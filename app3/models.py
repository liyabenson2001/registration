from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    Username=models.CharField(max_length=220)
    Email=models.EmailField(max_length=220)
    Password=models.CharField(max_length=8)
    Confirm_Password=models.CharField(max_length=8)



class Login(models.Model):
    Username=models.CharField(max_length=220)
    Password=models.CharField(max_length=8)
