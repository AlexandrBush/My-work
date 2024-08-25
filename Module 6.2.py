class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Создание атрибута класса __COLOR_VARIANTS,
    # который содержит список допустимых цветов для окрашивания.

    def __init__(self, owner, model, color, engine_power):   # Метод принимает четыре параметра и Устанавливает
        # приватные атрибуты
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):  # Возвращает строку с названием модели транспорта.
        return f"Модель: {self.__model}"

    def get_horsepower(self):  # Возвращает строку с мощностью двигателя.
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):  # Возвращает строку с цветом транспорта.
        return f"Цвет: {self.__color}"

    def print_info(self):  # Выводит информацию о модели, мощности двигателя, цвете и владельце транспорта.
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):  # Принимает параметр new_color и изменяет цвет транспорта,
        # если новый цвет находится в списке допустимых цветов. Если цвет не допустим, выводит сообщение об ошибке.
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):  # Класс Sedan наследуется от класса Vehicle.
    __PASSENGERS_LIMIT = 5  # Создание атрибута класса __PASSENGERS_LIMIT, который устанавливает максимальное
    # количество пассажиров для седана. Только зачем нам эта информация???

    def __init__(self, owner, model, color, engine_power):  # Метод __init__ принимает четыре параметра
        super().__init__(owner, model, color, engine_power)  # Вызывает метод __init__ родительского класса Vehicle
        # для установки атрибутов.


# Пример использования
vehicle1 = Sedan('Urban', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Student'

# Проверяем что поменялось
vehicle1.print_info()