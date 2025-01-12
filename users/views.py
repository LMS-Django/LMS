from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserCreatingForm, UserLoginForm
from .models import CustomUser


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
        
        return redirect('register')

    else:
        form = UserCreatingForm()

    return render(request, "users/register_page.html", {'form': form, 'title': 'Регистрация'})


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
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

    return render(request, 'users/login_page.html', {'form': form, 'title': 'Вход в аккаунт'})


@login_required(login_url='register')
def get_profile_page(request):
    if request.user.is_superuser:
        return redirect('register')
    return render(request, 'users/profile.html', {'user_data': str(request.user).split()})


def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'users/logout.html')

# Create your views here.
