from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course, Theme

admin.site.register(Course)
admin.site.register(Theme)

# Register your models here.
