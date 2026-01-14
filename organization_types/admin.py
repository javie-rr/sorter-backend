from django.contrib import admin
from organization_types.models import OrganizationType

# Register your models here.

@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']