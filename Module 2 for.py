numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# пустые списки
primes = []
not_primes = []
# при помощи цикла for перебираем список numbers с помощью переменной num
for num in numbers:
    # если переменная больше 1, то значение правдивое, проверка на простоту числа
    if num > 1 == True:
        # указываем длинну проверки списка для переменной i начиная с 2
        for i in range(2, num):
            # если остаток от деления равен нулю, значит число делится нацело и не является простым
            if num % i == False:
                # добавляем число в список not_primes
                not_primes.append(num)
                break  # остановка цикла

        else:
            # добавляем число в список primes
            primes.append(num)

# выводим списки primes и not_primes
print('primes:', primes)
print('not_primes:', not_primes)
