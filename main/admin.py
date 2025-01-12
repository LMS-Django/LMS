from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course, Theme, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name')  # Указываем поля для отображения
    ordering = ('first_name', 'last_name', 'email')  # Используем email вместо username
    search_fields = ('first_name', 'last_name')  # На

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )


admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
