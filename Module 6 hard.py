import math  # Импортируем модуль math, чтобы использовать функции из него.

class Figure:  # Создаём класс Figure.
    sides_count = 0  #статическое поле, указывающее количество сторон фигуры.

    def __init__(self, color, *sides):  # инициализирует цвет и стороны фигуры. Если количество переданных сторон не совпадает с sides_count, то стороны устанавливаются в единицы.
        self.__color = list(color)
        self.filled = True
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):  # возвращает текущий цвет фигуры.
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверяет, что значения RGB цветов находятся в допустимом диапазоне.
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):  # устанавливает новый цвет, если он проходит проверку.
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):  # проверяет, что количество и значения сторон корректны.
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):  # возвращает текущие стороны фигуры.
        return self.__sides

    def __len__(self):  # возвращает периметр фигуры.
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # устанавливает новые стороны, если они проходят проверку.
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):  # Наследует от Figure и переопределяет sides_count на 1.
    sides_count = 1

    def __init__(self, color, radius):  # инициализирует радиус круга.
        super().__init__(color, radius)
        self.__radius = radius

    def get_square(self):  # вычисляет площадь круга.
        return math.pi * self.__radius ** 2

class Triangle(Figure):  # Наследует от Figure и переопределяет sides_count на 3.
    sides_count = 3

    def get_square(self):  # вычисляет площадь треугольника.
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):  # Наследует от Figure и переопределяет sides_count на 12.
    sides_count = 12

    def __init__(self, color, side): # инициализирует все стороны куба одинаковыми значениями.
        super().__init__(color, *([side] * self.sides_count))

    def get_volume(self):  # вычисляет объём куба.
        side = self.get_sides()[0]
        return side ** 3

# Примеры использования:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216