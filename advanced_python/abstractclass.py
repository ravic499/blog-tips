"""
Module to explain abstract class and methods in Python

Define a abstract class and abstract method with an example 
"""


from abc import ABC, abstractmethod

# 1. Example using living beings
class Animal(ABC):

    @abstractmethod
    def birth_style(self):
        pass

class Mammals(Animal):

    def birth_style(self):
        print("Live Birth")

class Reptiles(Animal):

    def birth_style(self):
        print("Hatch Eggs")

m = Mammals()
m.birth_style()

# Output
# Live Birth

r = Reptiles()
r.birth_style()

# Output
# Hatch Eggs 
 
# 2. Example using mathematics
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side 


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

s = Square(5)
print(s.area())

# Output
# 25

c = Circle(2)
print(c.area())

# Output
# 12.56
