""""""
"""
OOP qism - class , object , method , attribute
OOP tamoil - class , object , inheritance , encapsulation , polymorphism , abstraction
ToDo
"""


#
# class ClassName:  # pascal case
#     a = 10  # class attribute
#
#     def __init__(self, b = None):  # CONSTRUCTURE
#         self.b = b  # class insta nce attribute
#
#     def add(self):  # method
#         return self.b + self.a
#
#
# print(ClassName(b=20).add())


# =====================================================

class Animal:
    def __init__(self, name, gender, habitat):
        self.name = name
        self.gender = gender
        self.habitat = habitat

    def about(self):
        text = f"""
            name : {self.name}
            gender : {self.gender}
            habitat : {self.habitat}"""

        return text


class Bird(Animal):
    def __init__(self, name, habitat, gender, fly):
        super().__init__(name, gender, habitat)
        self.fly = fly

    def about(self):
        return super().about() + f"\n\t\t\tfly : {self.fly}"


b = Bird("Qarg'a", gender='F', habitat='tree', fly=True)
print(b.about())


class Mammal:
    pass


class Fish(Bird, Mammal):
    pass


f = Fish("Uchar baliq", 'water', 'M', True)
print(f.about())
