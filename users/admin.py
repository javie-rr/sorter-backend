from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = ['id','first_name','last_name','second_last_name','email','password']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Personal info', {
            'fields': ('second_last_name',),
        }),
    )

    # To include the new field in the add user form as well
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Personal info', {
            'fields': ('first_name','last_name','second_last_name',),
        }),
    )