from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    list_display = ('email', 'first_name', 'last_name', 'user_type')
    ordering = ('last_name', 'first_name', 'email')
    list_filter = ('user_type',)
