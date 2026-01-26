from django.db import models
from area_types.models import AreaType

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    area_type = models.ForeignKey(
       AreaType,
        on_delete=models.PROTECT,
        related_name="areas"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="subareas",
    )


    def __str__(self):
        return self.name