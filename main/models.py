import datetime

from django.db import models


class Course(models.Model):

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Course ' + self.name + ' ' + str(self.id)
    

class Topic(models.Model):

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    name = models.CharField(max_length=50)
    open = models.BooleanField(default=False)
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)


class Lection(models.Model):

    class Meta:
        verbose_name = 'Лекционный материал'
        verbose_name_plural = 'Лекционные материалы'

    name = models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=datetime.datetime.now() \
                                    + datetime.timedelta(days=14))
    topic = models.ForeignKey(Topic, related_name='tasks', on_delete=models.CASCADE)


class Hometask(models.Model):

    class Meta:
        verbose_name = 'Домашнее задание'