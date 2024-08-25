# Метод isinstance() в Python используется для проверки принадлежности объекта к определенному классу или типу данных

def calculate_structure_sum(data):
    total_sum = 0
    # разбор по элементам
    for element in data:
        # проверка чисел,чисел с плавающей точкой
        if isinstance(element, (int, float)):
            total_sum += element
        # проверка строк
        elif isinstance(element, str):
            total_sum += len(element)
        # список,кортеж,множества
        elif isinstance(element, (list, set, tuple)):
            total_sum += calculate_structure_sum(element)
        # рекурсивно проверка словаря(Рекурсия — это техника в программировании, при которой функция вызывает сама себя для решения подзадачи, которая является частью исходной задачи.)
        elif isinstance(element, dict):
            for key, value in element.items():
                total_sum += calculate_structure_sum([key, value])

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)