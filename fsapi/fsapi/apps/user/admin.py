from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, _
from .models import UserInfo, Credit


class UserModelAdmin(UserAdmin):
    list_display = (
        "id", 'username', "nickname", "avatar_small", "email", "mobile",
        "money", "credit",
        "is_superuser", 'is_staff',
    )
    # 可以在列表页就直接更改的属性
    list_editable = ["credit", "money"]

    # fieldsets 和 add_fieldsets 都在从UserAdmin中复制粘贴过来，重写加上自己需要的字段的。
    fieldsets = (
        (None, {'fields': ('username', 'password', 'avatar')}),
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

    def save_model(self, request, obj, form, change):
        if change:
            """更新数据"""
            user = UserInfo.objects.get(pk=obj.id)
            has_credit = user.credit  # 原来用户的积分数据
            new_credit = obj.credit  # 更新后用户的积分数据

            Credit.objects.create(
                user=user,
                number=int(new_credit - has_credit),
                operation=2,
            )

        obj.save()

        if not change:
            """新增数据"""
            Credit.objects.create(
                user=obj.id,
                number=obj.credit,
                operation=2,
            )


admin.site.register(UserInfo, UserModelAdmin)


class CreditModelAdmin(admin.ModelAdmin):
    """积分流水的模型管理器"""
    list_display = ["id", "user", "number", "__str__"]


admin.site.register(Credit, CreditModelAdmin)
