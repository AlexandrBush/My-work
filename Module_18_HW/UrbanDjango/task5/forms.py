from django import forms

# Создаем класс UserRegister, который наследуется от forms.Form
# Этот класс определяет форму для регистрации пользователя
class UserRegister(forms.Form):
    # Поле для ввода логина пользователя
    # max_length=30 — ограничение на максимальную длину логина (30 символов)
    # label="Введите логин" — текст, который будет отображаться рядом с полем ввода
    username = forms.CharField(max_length=30, label="Введите логин")

    # Поле для ввода пароля
    # widget=forms.PasswordInput — указывает, что это поле будет скрыто (точки вместо символов)
    # min_length=8 — минимальная длина пароля (8 символов)
    # label="Введите пароль" — текст, который будет отображаться рядом с полем ввода
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Введите пароль")

    # Поле для повторного ввода пароля
    # Аналогично полю password, но с другим текстом label
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Повторите пароль")

    # Поле для ввода возраста пользователя
    # forms.IntegerField — поле для ввода целого числа
    # label="Введите свой возраст" — текст, который будет отображаться рядом с полем ввода
    age = forms.IntegerField(label="Введите свой возраст")