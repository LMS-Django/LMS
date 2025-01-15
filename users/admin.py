# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'first_name', 'last_name')
#     ordering = ('last_name', 'first_name', 'email')
#     search_fields = ('email', 'first_name', 'last_name')

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
#         }),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
