from django.urls import path

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('create_course', views.create_course, {'name': 'Первый тестовый курс'}, 
         name='create-course'),
    path('get_all_courses', views.get_all_courses, name='get-courses'),
    path('get_course/<int:pk>', views.get_course, name='get-course'),
    path('register', views.register, name='register'),
    path('profile', views.get_profile_page, name='profile'),
    path('logout', views.logout_view, name='logout')
]
