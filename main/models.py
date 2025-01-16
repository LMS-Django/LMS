from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="courses"
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


class Assignment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    file = models.FileField(upload_to="assignments/files/", null=True, blank=True)

    def __str__(self):
        return self.title


class StudentsGroup(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students_groups")
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="students_groups")

    def __str__(self):
        return f"{self.name} ({self.course.title})"


class Attendance(models.Model):
    group = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE, related_name="attendance_records")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.is_present}"


class Homework(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="homework/files/", null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"