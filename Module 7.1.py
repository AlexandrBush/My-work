'Задача "Учёт товаров":'


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):                          # возвращает строку в формате <название>, <вес>, <категория>
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'       # инкапсулированный атрибут

    def get_products(self):                          # открывает файл __file_name для чтения, считывает все строки
                                                     # и возвращает их в виде единой строки.
        with open(self.__file_name, 'r') as file:
            products = file.readlines()
        return ''.join(products)

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str in existing_products:
                    print(f'Продукт {product_str} уже есть в магазине')
                else:
                    file.write(product_str + '\n')

# принимает неограниченное количество объектов класса Product.
# Он сначала получает все существующие продукты из файла, затем проверяет каждый переданный продукт на
# наличие в файле. Если продукт уже есть, выводит сообщение об этом, иначе добавляет продукт в файл.


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
