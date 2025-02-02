from django.contrib import admin

from apps.users.models import CustomUser


class UserManager(admin.ModelAdmin):
    model = CustomUser
    admin.site.register(CustomUser)