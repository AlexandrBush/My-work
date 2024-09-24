def apply_all_func(int_list, *funtions):
    results = {}

    for func in funtions:
        # Вызывам функцию и сохраняем результат в словарь
        results[func.__name__] = func(int_list)

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))