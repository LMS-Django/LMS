from django.db import models
from django.conf import settings

from .exceptions import NoDataError, ExessDataError

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="courses",
        limit_choices_to={'user_type': 'teacher',
                          'is_superuser': False}
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="enrolled_courses",
        blank=True,
        limit_choices_to={'user_type': 'student',
                        'is_superuser': False}
    )

    def __str__(self):
        return self.title


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class Task(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="assignments", default='')
    title = models.CharField(default='h', max_length=255)
    description = models.TextField(default='hello')
    due_date = models.DateField(default='2002-11-11')
    need_homework = models.BooleanField(default=False)
    file = models.FileField(upload_to="assignments/files/", null=True, blank=True)
    url = models.URLField(default='', blank=True)


    # def clean(self):
    #     if not self.file and not self.url:
    #         raise NoDataError('Загрузите данные')
        
    #     if self.file and self.url:
    #         raise ExessDataError('Надо загрузить либо ссылку, либо файл')

    def __str__(self):
        return self.title


class Homework(models.Model):
    MARKS = [
        ('0', 'не проверено'),
        ('2', 'неудовлетворительно'),
        ('3', 'удовлетворительно'),
        ('4', 'хорошо'),
        ('5', 'отлично')
    ]

    assignment = models.ForeignKey(Task, on_delete=models.SET_NULL, related_name="submissions", null=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="homework/files/", null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    mark = models.CharField(max_length=3,
                            choices=MARKS,
                            default='0')
    teacher_comment = models.TextField(null=True)

    def __str__(self):
        return f"{self.student.email} - {self.assignment.title}"
