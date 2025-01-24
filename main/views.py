import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .exceptions import NoDataError, ExessDataError
from .forms import ChooseStudentsForm, AssignmentUpload, TopicCreatingForm
from .models import Course, Topic, Task

from users.models import CustomUser


def is_teacher(user):
    return user.user_type == 'teacher'


def is_student(user):
    return user.user_type == 'student'


def main_page(request):
    return render(request, 'main/main.html', {'auth': request.user.is_authenticated})


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


@login_required(login_url='login_student')
def get_course(request, pk):
    if is_teacher(request.user):
        return redirect('change_course', pk=pk)
    
    elif is_student(request.user):
        try:
            course = Course.objects.get(id=pk)
        except:
            return render(request, 'main/404.html')

        return render(request, 'main/course_details.html', {'course': course})


@login_required(login_url='login_student')
def add_students(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except:
        return render(request, 'main/404.html')
    
    if request.method == 'POST':
        form = ChooseStudentsForm(request.POST, course=course)
        if form.is_valid():
            selected_options = form.cleaned_data['options']
            student_ids = [student.id for student in CustomUser.objects.filter(id__in=selected_options)]
            print(student_ids)

            for student_id in student_ids:
                student = CustomUser.objects.get(id=student_id)
                course.students.add(student)

            return redirect('course_detail', pk=pk)
            
    else:
        form = ChooseStudentsForm(course=course)

    students = CustomUser.objects.filter(user_type='student').exclude(enrolled_courses=course)
    not_superusers = [(str(student.id), student) for student in students if not student.is_superuser]

    return render(request, 'main/add_students.html', {'form': form, 
                                                      'is_empty': len(not_superusers) == 0,
                                                      'course': course})


@login_required(login_url='main')
def change_course(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'main/404.html')

    return render(request, 'main/change_course.html', {'course': course})


def upload_assignment(request, pk):
    '''
    Загрузка задания. При нажатии кнопки происходит переход на страницу с формой
    для заполнения. Должно быть представлено только одно вложение: либо ссылка, либо 
    файл.
    '''
    topic = Topic.objects.get(id=pk)
    if request.method == 'POST':
        form = AssignmentUpload(request.POST, request.FILES)
        if form.is_valid():
            

            new_task = form.save(commit=False)
            new_task.topic = topic
            new_task.save()
        
            # if file and url:
            #     messages.error(request, 'Нужно заполнить только одно поле: файл/ссылка на диск.')
            #     return redirect(upload_assignment)
        
            return redirect('profile')
        
    else:
        form = AssignmentUpload()

    return render(request, 'main/upload_task.html', {'form': form})


def get_assignment(request, pk):
    assignment = Task.objects.get(id=pk)
    # print(assignment)
    return render(request, 'main/get_task.html', {'assignment': assignment})


def add_topic(request, pk: int):
    '''
    Добавление темы в курс, при нажатии кнопки выполняется переход на страницу формы.
    По окончании добавления происходит переход обратно на страницу курса.

    :param pk: id курса, для которого добавляется тема.
    '''

    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = TopicCreatingForm(request.POST)
        if form.is_valid():
            
            new_topic = form.save(commit=False)
            new_topic.course = course
            new_topic.save()

            return redirect('change_course', course.id)

    else:
        form = TopicCreatingForm()

    return render(request, 'main/add_topic.html', {'form': form})


def change_task(request, pk, task_pk):
    topic = Topic.objects.get(id=pk)
    task = Task.objects.get(id=task_pk)
    if request.method == 'POST':
        form = AssignmentUpload(request.POST, request.FILES, instance=task)
        if form.is_valid():
            
            print(form.cleaned_data)
            # new_task = form.save(commit=False)
            # new_task.topic = topic
            # new_task.save()
        
            # if file and url:
            #     messages.error(request, 'Нужно заполнить только одно поле: файл/ссылка на диск.')
            #     return redirect(upload_assignment)
        
            return redirect('profile')
        
    else:
        form = AssignmentUpload()

    return render(request, 'main/change_task.html', {'form': form, 'task_id': task.id, 'topic_id': topic.id})


def delete_task(request, pk, task_pk):
    task = Task.objects.get(id=task_pk)
    topic = Topic.objects.get(id=pk)
    course = topic.course
    if request.method == 'POST':
        task.delete()
        return redirect('change_course', course.id)
    
    return render(request, 'main/delete_task.html')
