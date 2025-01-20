from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from .models import Course, Topic
from .forms import ChooseStudentsForm

from users.models import CustomUser

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


@login_required(login_url='register')
def get_course(request, pk):
    if request.user.user_type == 'teacher':
        return redirect('change_course')
    elif request.user.user_type == 'student':
        course = Course.objects.get(id=pk)
        return render(request, 'main/course_details.html', {'course': course})


def change_course(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except:
        return render(request, 'main/404.html')
    
    if request.method == 'POST':
        form = ChooseStudentsForm(request.POST, course=course)
        if form.is_valid():
            selected_options = form.cleaned_data['options']
            selected_names = [student for student in CustomUser.objects.filter(id__in=selected_options)]
            print(selected_names)
            if selected_options:
                return HttpResponse(f"Вы выбрали: {', '.join(list(map(str, selected_names)))}")
            else:
                return HttpResponse("Вы не выбрали опции.")
    else:
        form = ChooseStudentsForm(course=course)

    return render(request, 'main/change_course.html', {'form': form, 'course': course})

