from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    #pass
    model = User
    list_display = ['id','first_name','last_name','second_last_name','email','password']