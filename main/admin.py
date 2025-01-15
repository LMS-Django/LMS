from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course, Topic

admin.site.register(Course)
admin.site.register(Topic)

# Register your models here.
