def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Функция для проверки, является ли число простым
        def check_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        if check_prime(result):
            print("Простое")
        else:
            print("Составное")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)