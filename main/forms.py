from django.forms import Form, CharField, EmailField, PasswordInput


class UserCreatingForm(Form):
    first_name = CharField(max_length=100, label='Имя')
    last_name = CharField(max_length=100, label='Фамилия')
    email_address = EmailField(max_length=100, label='Электронная почта')
    password = CharField(widget=PasswordInput, label='Пароль')
