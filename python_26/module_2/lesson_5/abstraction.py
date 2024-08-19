# class Base:
#     def random_number(self):
#         return 10
from abc import ABC, abstractmethod


# class Child:
#     def random_number1(self):
#         self.a = 20
#         return 10
#
#     def random_number2(self):
#         return self.random_number1() + 20


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def area2(self):
        pass


class Circle(Shape):
    def area(self):
        pass

    def area2(self):
        pass

    def add(self):
        pass


obj = Circle()
print(obj)
