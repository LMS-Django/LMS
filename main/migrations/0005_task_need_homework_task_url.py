# Generated by Django 5.1.4 on 2025-01-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='need_homework',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
