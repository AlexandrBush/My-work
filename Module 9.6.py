def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def all_variants(text):
    n = len(text)
    fib = fibonacci()
    next(fib)  # Пропускаем первое число Фибоначчи (0)

    # Генерируем подпоследовательности всех возможных длин
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            yield text[i:i + length]


# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)