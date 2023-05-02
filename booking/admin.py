from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import HuezoosUser
# # Register your models here.

class AdminHuezoosUser(UserAdmin):
    ordering = ('email',)
    list_display = ('email',)
    pass


admin.site.register(HuezoosUser, AdminHuezoosUser)