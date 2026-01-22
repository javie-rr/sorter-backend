from django.contrib import admin
from area_types.models import AreaType

# Register your models here.

@admin.register(AreaType)
class AreaTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']