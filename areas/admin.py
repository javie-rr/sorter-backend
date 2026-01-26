from django.contrib import admin
from areas.models import Area

# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id','name','area_type','parent']