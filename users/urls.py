from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.custom_login, name='login_stud'),
    path('login', views.custom_login, name='login_teacher'),
    path('profile', views.get_profile_page, name='profile'),
    path('logout', views.custom_logout, name='logout'),
    path('reset_password', views.password_reset, name='password_reset') 
]
