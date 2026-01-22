from django.db import models

# Create your models here.

class Address(models.Model):
    postal_code = models.CharField(max_length=10)
    state = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, blank=True, null=True)
    street_type = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    external_number = models.CharField(max_length=20)
    internal_number = models.CharField(max_length=255, blank=True, null=True)
    cross_streets = models.CharField(max_length=255, blank=True, null=True)