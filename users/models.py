from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    second_last_name = models.CharField(max_length=200)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True) 
    email = models.EmailField(max_length=320, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'second_last_name', 'username', 'rfc', 'curp']