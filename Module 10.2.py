import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.total_enemies = 100  # У каждого рыцаря свои 100 врагов

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.total_enemies > 0:
            time.sleep(1)  # Имитация 1 дня сражения
            self.days += 1
            self.total_enemies -= self.power
            if self.total_enemies < 0:
                self.total_enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


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
