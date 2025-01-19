from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from .models import Course, Topic

def is_teacher(user):
    return user.user_type == 'teacher'

def is_student(user):
    return user.user_type == 'student'


def main_page(request):
    return render(request, 'main/main.html')


def view_all_courses(request):
    if not request.user.is_authenticated:
        return render(request, 'main/404.html')
    
    if is_teacher(request.user):
        courses = Course.objects.all()
        my_courses = []
        for course in courses:
            if course.teacher == request.user:
                my_courses.append(course)
    
    elif is_student(request.user):
        courses = Course.objects.all()
        my_courses = []
        for course in courses:
            if course.teacher == request.user:
                my_courses.append(course)

    return render(request, 'all_courses_list.html', {'courses': my_courses})



# def change_course(request, id):


def get_all_courses(request):
    courses = Course.objects.all()
    str_courses = ''
    for course in list(courses):
        str_courses += str(course)

    return redirect('main')
    # return HttpResponse(f'all courses {str_courses}')


def get_course(request, pk):
    course = Course.objects.get(id=pk)
    return HttpResponse(f'course {str(pk)} {str(course)}')
