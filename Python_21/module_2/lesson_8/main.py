# classmethod
# staticmethod
# property

# class File:
#     def __init__(self ,a):
#         self.a = a
#
#     @classmethod
#     def read(cls , id , name):
#         return cls.__name__.lower()[:-3]+"s.txt"
#
#     @staticmethod
#     def write(self ,data):
#         pass

# File().read() # File

# class UserDTO(File):
#     def __init__(self , id=None , name=None):
#         self.id = id
#         self.name = name
#
#
# print(UserDTO.read(1, "Botir"))

# class Animal:
#
#     @staticmethod
#     def add(x , y):
#         return x + y
#
#
# class Fish(Animal):
#     pass
#
#
# print(Fish().add(1, 2))
