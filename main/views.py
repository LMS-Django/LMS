from django.http import HttpResponse
from django.shortcuts import render, redirect


from .models import Course, Topic


def main_page(request):
    return render(request, 'main/main.html')


def create_course(request, name):
    new_course = Course.objects.create(name=name)
    return HttpResponse(f'created course object {new_course}')


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
