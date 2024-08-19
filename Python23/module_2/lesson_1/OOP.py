"""
class
obj
__init__ konstruktr
methods
__repr__
__str__
"""


# PascalCase
# class ClassName:
#     pass

# a = 10
# str()
# a = "LL" # object
# a.lower() # method

# python -> class , obj


# class User:
#     name = "Botir" # class attribute
#     age = 30 # class attribute
#
# user1 = User() # object
# user2 = User() # object
# print(user1.name)
# print(user1.age)
# print(user2.name)

# ==================================

# class User:
#     pi = 3.14  # class attribute
#
#     def __init__(self, name: str, age: int = 30) -> None:
#         self.name = name  # class instant attribute
#         self.age = age  # class instant attribute


# user1 = User("Botir" , 35)
# user2 = User("Kamol" , 30)
# users : tuple[User] = (user1 , user2)
#
# for u in users:
#     print(u.name)


# students = []
#
#
# class Student:
#     def __init__(self, id, name, age, group_number, course, address):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.group_number = group_number
#         self.course = course
#         self.address = address
#
#     def save(self):
#         students.append(self)
#
#     def delete(self):
#         for student in students:
#             if student.id == self.id:
#                 students.remove(student)
#
#     def update(self, field , new_val):
#         for student in students:
#             if student.id == self.id:
#                 if field == 'name':
#                     student.name = new_val
#                 if field == "age":
#                     student.age = new_val
#                 if field == "group_number":
#                     student.group_number = new_val
#
#     def get(self) -> User:
#         for student in students:
#             if student.id == self.id:
#                 return student


# s1 = Student(1, "Murod", 21, "P23", "PYTHON", "Tashkent Chorsu")
# s1.save()
#
# print(s1.get().id)

# s2 = Student(2, "Ravshan", 26, "F21", "FOUNDATION", "Tashkent Sergili")

# s1.save()
# print(s1.name)
# s1.update("name" , 'Kamron')
# print(s1.name)
# print(students[0].name)
# s1.delete()

# s1 = Student("Murod" , 21 ,"p23"  , "PYTHON" , "Tashkent Chorsu")
# print(s1)
# s1.year = 2002
# s2 = Student("Murod" , 21 ,"p23"  , "PYTHON" , "Tashkent , Chorsu")
