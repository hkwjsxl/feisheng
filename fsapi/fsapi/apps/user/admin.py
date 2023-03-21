from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo


class UserModelAdmin(UserAdmin):
    list_display = (
        'username', "nickname", 'email', "mobile",
        "is_superuser", 'is_staff',
    )


admin.site.register(UserInfo, UserModelAdmin)
