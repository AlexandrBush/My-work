"""Мифическое наследование"""


class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь по горизонтали
        self.sound = 'Frrr'  # звук, который издаёт Horse

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полёта по вертикали
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт Eagle

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):  # Класс Pegasus наследуется от Horse и Eagle. Это означает, что он получает
    # все атрибуты и методы обоих классов.
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# Пример использования
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
