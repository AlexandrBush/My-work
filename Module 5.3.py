"""
Задача "Нужно больше этажей":

"""


class House:  
  
  def __init__(self, name, floors):
      self.name = name
      self.floors = floors

  def __str__(self):  
      return f"Название: {self.name}, кол-во этажей: {self.floors}"

  def __eq__(self, other):
      if isinstance(other, House):
          return self.floors == other.floors
      
  def __lt__(self, other):
      if isinstance(other, House):
          return self.floors < other.floors
      
  def __le__(self, other):
      if isinstance(other, House):
          return self.floors <= other.floors
      
  def __gt__(self, other):
      if isinstance(other, House):
          return self.floors > other.floors
      
  def __ge__(self, other):
      if isinstance(other, House):
          return self.floors >= other.floors

  def __ne__(self, other):
      if isinstance(other, House):
          return self.floors != other.floors     

  def __add__(self, value):
      if isinstance(value, int):
          self.floors += value
      return self

  def __radd__(self, value):
      return self.__add__(value)

  def __iadd__(self, value):
      return self.__add__(value)

# Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
