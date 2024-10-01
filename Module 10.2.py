import threading
import time


class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")

        while Knight.total_enemies > 0:
            days += 1
            Knight.total_enemies -= self.power
            print(f"{self.name}, сражается {days} день(дня)..., осталось {Knight.total_enemies} воинов.")
            time.sleep(1)  # Имитация одного дня сражения

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")