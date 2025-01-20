from django.forms import Form, CharField, EmailField, PasswordInput, MultipleChoiceField, SelectMultiple


class UserCreatingForm(Form):
    first_name = CharField(max_length=100, label='Имя')
    last_name = CharField(max_length=100, label='Фамилия')
    email_address = EmailField(max_length=100, label='Электронная почта')
    password = CharField(widget=PasswordInput, label='Пароль')


class UserLoginForm(Form):
    email_address = CharField(max_length=100, label='Электронная почта')
    password = CharField(widget=PasswordInput, label='Пароль')


class PasswordResetForm(Form):
    password = CharField(widget=PasswordInput, label='Пароль')
    password_confirm = CharField(widget=PasswordInput, label='Подтверждение пароля')

