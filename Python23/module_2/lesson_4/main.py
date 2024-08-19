""""""
from math import pi

"""
OOP tamoillari
    class 
    object
    inheritance
    encapsulation
    polymorphism
    abstraction
    
encapsulation
    attribute
        public     -> attribute   
            
        protected  -> _attribute
            
        private    -> __attribute 
        
"""


# def func1(x)

# polymorphism -> overloading , overriding

# python -> dynamic
# Java -> static

# def func1(x):
#     return x

# def func1(x, y):
#     return x + y


# # Python -> overriding
# # Java   -> overloading
#
# # func1(1,2)
#
#
# #
# # class str:
# #     def __init__(self, value):
# #         self.value = value
# #
# #     def __len__(self):
# #         c = 0
# #         for _ in self.value:
# #             c += 1
# #         return c
# #
# # class list:
# #     def __init__(self, value):
# #         self.value = value
# #     def __len__(self):
# #         return len(self.value)
# #
# #
# # a = list([1,2,3,4,5])
# # print(len(a))
#
#
# class Animal:
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Wof !"
#
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow !"
#
# d = Dog()
# print(d.speak())
#
# c = Cat()
# print(c.speak())

# class Shape:
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 2*pi*self.radius**2
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side**2
#
# class Triangle(Shape):
#     def __init__(self, base , hight):
#         self.base = base
#         self.hight = hight
#
#     def area(self):
#         return self.base * self.hight / 2
#
# print(Square(2).area())


class CRUD:
    def save(self):
        pass

    def get(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


users = []


class User(CRUD):
    def save(self):
        users.append(self)

    def get(self):
        super().get()

    def update(self):
        super().update()

    def delete(self):
        super().delete()


todos = []


class ToDo(CRUD):
    def save(self):
        todos.append(self)

    def get(self):
        super().get()

    def update(self):
        super().update()

    def delete(self):
        super().delete()
