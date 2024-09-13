# Домашнее задание по уроку "Try и Except"


def add_everything_up(a, b):
    try:
        # Попытка сложить числа
        return a + b
    except TypeError:
        # Если возникла ошибка TypeError, значит типы данных разные
        return f"{a}{b}"


# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456
