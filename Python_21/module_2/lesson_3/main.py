# class , object


# class ClassName:
#     a = 10
#
#     def __str__(self):
#         pass
#
#     def __repr__(self):
#         pass

# obj = ClassName()
# print(obj.a)
# obj.a = 20
# print(obj.a)
# print(obj.__class__.__name__)

"""
inheritance OOP
"""


class Animal:
    def __init__(self , name , gender , habitat):
        self.name = name
        self.gender = gender
        self.habitat = habitat

    def print_name(self):
        print(self.name)




class Bird:
    def __init__(self, name, gender, habitat, fly: bool):
        self.name = name
        self.gender = gender
        self.habitat = habitat
        self.fly = fly


class Fish(Animal ,Bird):
    def __init__(self, name, gender, habitat, fly):
        Animal.__init__(self , name , gender , habitat)
        Bird.__init__(self , name , gender , habitat ,fly)
        self.fly = fly

f = Fish("nimdir" , "M" , "Tree" , True)
print(f.name)
#
# b1 = Fish("To'ti qush" , "M" , "cage", True)
# b1.print_name()

