from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserCreatingForm
from .models import Course, CustomUser, Theme


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


def register(request):
    if request.method == 'POST':
        form = UserCreatingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.create_user(first_name=name, 
                                                  last_name=last_name,
                                                  email=email,
                                                  password=password)
            except:
                form = UserCreatingForm(request.POST)

            else:
                login(request, user)
        
        return redirect('main')

    else:
        form = UserCreatingForm()

    return render(request, "main/form.html", {"form": form})


@login_required(login_url='register')
def get_profile_page(request):
    print(request.user)
    return render(request, 'main/profile.html', {'user_data': str(request.user).split()})


def logout_view(request):
    logout(request)
    return redirect('main')
