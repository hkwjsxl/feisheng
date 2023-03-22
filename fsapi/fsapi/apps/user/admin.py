from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, _
from .models import UserInfo


class UserModelAdmin(UserAdmin):
    list_display = (
        "id", 'username', "nickname", "avatar_small", "email", "mobile",
        "money", "credit",
        "is_superuser", 'is_staff',
    )
    # fieldsets 和 add_fieldsets 都在从UserAdmin中复制粘贴过来，重写加上自己需要的字段的。
    fieldsets = (
        (None, {'fields': ('username', 'password', 'avatar_small')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    ordering = ('id',)


admin.site.register(UserInfo, UserModelAdmin)
