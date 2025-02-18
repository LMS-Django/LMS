from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('view_all_courses', views.view_all_courses, name='view_courses'),
    path('get_course/<int:pk>', views.get_course, name='course_detail'),
    path('add_students/<int:pk>', views.add_students, name='add_students'),

    path('get_assignment/<int:pk>', views.upload_homework, name='get_assignment'),
    path('change_course/<int:pk>', views.change_course, name='change_course'),
    path('change_course/<int:pk>/add_topic', views.add_topic, name='add_topic'),
    path('change_course/<int:pk>/change_topic/<int:topic_pk>', views.change_topic, name='change_topic'),
    path('change_course/<int:pk>/delete_topic/<int:topic_pk>', views.delete_topic, name='delete_topic'),

    path('change_topic/<int:pk>/add_assignment', views.upload_assignment, name='upload_assignment'),
    path('change_topic/<int:pk>/change_task/<int:task_pk>', views.change_task, name='change_task'),
    path('change_topic/<int:pk>/delete_task/<int:task_pk>', views.delete_task, name='delete_task'),

    path('rate_homework/<int:pk>', views.rate_homework, name='rate_homework'),

    path('checked_homeworks', views.checked_homeworks, name='checked_homeworks')
]
