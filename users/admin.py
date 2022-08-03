from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_employee', 'is_staff']


admin.site.register(User, UserAdmin)
