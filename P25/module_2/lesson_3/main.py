# class Animal:
#     def __init__(self, name, gender, habitat):
#         self.name = name
#         self.gender = gender
#         self.habitat = habitat
#
# class Bird(Animal):
#     def __init__(self,name, gender, habitat):
#         super().__init__(name, gender, habitat)
#
# class Fish(Animal):
#     def __init__(self,name, gender, habitat):
#         super().__init__(name, gender, habitat)
#
# class Mammal(Animal):
#     def __init__(self,name, gender, habitat):
#         super().__init__(name, gender, habitat)

# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#
# class B(A):
#     def __init__(self, a, b):
#         super

# class Animal:
#     def __init__(self, name, gender, habitat):
#
#
# class Bird(Animal):
#     def __init__(self,name, gender, habitat):
#         super().__init__(name, gender, habitat)



class Person:
    def __init__(self , fullname , phone_number , email , username , password, address):
        self.fullname = fullname
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.address = address
        self.address = address


class Customer(Person):
    def __init__(self, fullname , phone_number , email , username , password, address , balance):
        super().__init__(fullname, phone_number, email, username, password, address)
        self.balance = balance


class Employee(Person):
    def __init__(self, fullname , phone_number , email , username , password, address , salary):
        super().__init__(fullname, phone_number, email, username, password, address)
        self.salary = salary


class Manager(Employee):
    def __init__(self, fullname , phone_number , email , username , password, address , salary , experience):
        self.experience = experience
        super().__init__(fullname, phone_number, email, username, password, address, salary)


class Developer(Employee):
    def __init__(self ,fullname , phone_number , email , username , password, address , salary , level ):
        super().__init__(fullname, phone_number, email, username, password, address, salary)
        self.level = level


class BasicClass:
    def __init__(self , id , created_at , updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

class Book(BasicClass):
    def __init__(self, created_at , updated_at , id ,photo_url , book_part ):
        super().__init__(id, created_at, updated_at)
        self.photo_url = photo_url
        self.book_part = book_part


class Unit:
    def __init__(self , created_at , updated_at , id):
        pass





