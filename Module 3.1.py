# 1. Создать переменную calls = 0 вне функций.
calls = 0


# 2. Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных
# двух функциях.
def count_calls():
    global calls
    calls += 1


# 3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result


# 4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


# 5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
print(string_info('Yagoda'))
print(string_info('Malina'))
print(is_contains('Nas', ['k', 'SeBe', 'manILA']))  # Urban ~ urBAN
print(is_contains('yagoda malina', ['letom nas', 'v gosty zvala']))  # No matchesh
# 6. Вывести значение переменной calls на экран(в консоль).
print(calls)






