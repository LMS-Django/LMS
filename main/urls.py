from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('view_all_courses', views.view_all_courses, name='view_courses'),
    path('get_course/<int:pk>', views.get_course, name='course_detail'),
]
