from django.db import models
from organization_types.models import OrganizationType

# Create your models here.

class Organization(models.Model):
    rfc = models.CharField(max_length=12,unique=True)
    legal_name = models.CharField(max_length=255)
    capital_regime = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255)
    organization_type = models.ForeignKey(
       OrganizationType,
        on_delete=models.PROTECT,
        related_name="organizations"
    )

    def __str__(self):
        return self.legal_name


class OrganizationRegistration(models.Model):
    registration_date = models.DateField(auto_now_add=True)
    registration_location = models.GenericIPAddressField()
    is_active = models.BooleanField(default=True)
    organization = models.OneToOneField(
      Organization,
      on_delete=models.CASCADE,
      related_name="registration"
    )

    def __str__(self):
        return f"Registro - {self.organization.legal_name}"