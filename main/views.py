from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserCreatingForm, UserLoginForm
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
            except IntegrityError:
                messages.error(request, 'Пользователь с такой почтой уже существует, попробуйте войти.')
                return redirect('register')
        
            login(request, user)
        
        return redirect('main')

    else:
        form = UserCreatingForm()

    return render(request, "main/register_page.html", {'form': form, 'title': 'Регистрация'})


def custom_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                messages.error(request, 'Пользователя с такой почтой не существует,' \
                               'попробуйте еще раз или зарегистрируйтесь.')
                return redirect('login')

            if user.check_password(password):
                login(request, user)
            
            else:
                messages.error(request, 'Неправильный пароль.')

            return redirect('profile')

    else:
        form = UserLoginForm()

    return render(request, 'main/login_page.html', {'form': form, 'title': 'Вход в аккаунт'})


@login_required(login_url='register')
def get_profile_page(request):
    if request.user.is_superuser:
        return redirect('register')
    print(request.user)
    return render(request, 'main/profile.html', {'user_data': str(request.user).split()})


# def custom_logout(request):
#     if request.method == 'POST':
#         form = ,
#     logout(request)
#     return render(request, 'main/logout.html', {'form': form})
