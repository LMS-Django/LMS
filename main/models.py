from django.db import models


class Theme(models.Model):

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    name = models.CharField(max_length=50)
    open = models.BooleanField(default=False)


class Course(models.Model):

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Course ' + self.name + ' ' + str(self.id)
