from django.contrib import admin
from .models import Course, Topic, Assignment, StudentsGroup, Attendance, Homework

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Assignment)
admin.site.register(StudentsGroup)
admin.site.register(Attendance)
admin.site.register(Homework)