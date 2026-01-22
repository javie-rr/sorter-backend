from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)