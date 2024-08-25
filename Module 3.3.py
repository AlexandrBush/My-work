# Задача "Распаковка"

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

print_params(b=25)
print_params(c=[1, 2, 3])

# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.

values_list = [54.32, 'Строка']
values_dict = {'a': 54.32, 'b': 'Строка'}

# 2.Распаковка параметров:
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

print_params(*values_list, 42)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типо
# Проверьте, работает ли print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

