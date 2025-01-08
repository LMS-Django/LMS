from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('create_course', views.create_course, {'name': 'Первый тестовый курс'}, 
         name='create-course'),
    path('get_all_courses', views.get_all_courses, name='get-courses'),
    path('get_course/<int:pk>', views.get_course, name='get-course'),

    path('register', views.register, name='register'),
    path('login', views.custom_login, name='login'),
    path('profile', views.get_profile_page, name='profile'),
    path('logout', views.custom_logout, name='logout')
]
