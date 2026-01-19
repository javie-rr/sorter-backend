from django.contrib import admin
from organizations.models import Organization, OrganizationRegistration

# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['rfc', 'legal_name', 'capital_regime', 'trade_name']