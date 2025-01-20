from django.shortcuts import render
from .forms import UserRegister

# Псевдо-список уже существующих пользователей
users = ['Vasya', 'Petya', 'Kolya']


# Функция для обработки регистрации с использованием Django-формы
def sign_up_by_django(request):
    # Создаем пустой словарь для хранения информации, которая будет передана в шаблон
    info = {}

    # Проверяем, был ли запрос методом POST (отправка формы)
    if request.method == 'POST':
        # Создаем экземпляр формы с данными из POST-запроса
        form = UserRegister(request.POST)

        # Проверяем, валидны ли данные формы
        if form.is_valid():
            # Извлекаем очищенные данные из формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем, совпадают ли пароли
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            # Проверяем, что возраст пользователя не менее 18 лет
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            # Проверяем, существует ли пользователь с таким логином
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            # Если все проверки пройдены, выводим сообщение об успешной регистрации
            else:
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
        else:
            # Если данные формы не валидны, добавляем сообщение об ошибке
            info['error'] = 'Неверные данные'
    else:
        # Если запрос не POST, создаем пустую форму для отображения
        form = UserRegister()

    # Добавляем форму в словарь info для передачи в шаблон
    info['form'] = form
    # Рендерим шаблон с передачей контекста (info)
    return render(request, 'fifth_task/registration_page.html', info)


# Функция для обработки регистрации без использования Django-формы (напрямую из HTML-формы)
def sign_up_by_html(request):
    # Создаем пустой словарь для хранения информации, которая будет передана в шаблон
    info = {}

    # Проверяем, был ли запрос методом POST (отправка формы)
    if request.method == 'POST':
        # Извлекаем данные из POST-запроса
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Проверяем, совпадают ли пароли
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        # Проверяем, что возраст пользователя не менее 18 лет
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        # Проверяем, существует ли пользователь с таким логином
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        # Если все проверки пройдены, выводим сообщение об успешной регистрации
        else:
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    # Рендерим шаблон с передачей контекста (info)
    return render(request, 'fifth_task/registration_page.html', info)