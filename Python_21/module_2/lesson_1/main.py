# def -> function
# class -> class


# class User:
#     name = "John" # class attribute
#     age = 25

    # def __str__(self):
    #     return self.name
#
# user1 = User()
# print(user1)
# print(user1.name)
# print(user1.age)
#
# user2 = User()
# print(user2.name)

# Product(name , price , color)
# 5 ta object

# class User:
#     a = 6 # class attribute
#     def __init__(self,name , age ):
#         self.name = name # class instance attribute
#         self.age = age # # class instance attribute


# user1 = User("John" , 25)
# user1.a = 10
# print(user1.a)
# user2 = User("Botir" , 24)
# print(user2.a)


# print(user1.a)
# print(user1.name , user1.age)
# user2 = User("Botir" , 24)
# print(user2.name , user2.age)
# print(user2.a)


# Product(name , price , color)
# 5 ta object
# class Product:
#     def __init__(self, name, price, color):
#         self.name = name
#         self.price = price
#         self.color = color

# p1 = Product("Iphone 15", 1800 , "black")
# p2 = Product("Iphone 14", 1300 , "green")
# p3 = Product("Iphone 13", 1000 , "blue")
# p4 = Product("Iphone 12", 700 , "white")
# p5 = Product("Iphone 11", 500 , "gray")
#
# products = []
# products.append(p1)
# products.append(p2)
# products.append(p3)
# products.append(p4)
# products.append(p5)
#
# for i in products:
#     print(i.name , i.color)

# products = []
# class Product:
#     def __init__(self, name, price, color):
#         self.name = name
#         self.price = price
#         self.color = color
#
#     def save(self):
#         products.append(self.__dict__)
#
#     def delete(self):
#         for product in products:
#             if product['name'] == self.name:
#                 products.remove(product)
#
# p1 = Product("Iphone 11" , 500 , "white")
# p2 = Product("Iphone 14" , 1200 , "white")
# p1.save()
#
# print(products)

# class MyStr:
#     def __init__(self, object: str):
#         self.object = object
#
#     def count(self, x, __start=None, __end=None):
#         if not __start:
#             __start = 0
#         if not __end:
#             __end = len(self.object)
#         c = 0
#         l = len(x)
#
#         for i in range(len(self.object[__start:__end]) - l):
#             if self.object[__start:__end][i:i + l] == x:
#                 c += 1
#         return c
#
#     def find(self, __sub, __start=None, __end=None):
#         if not __start:
#             __start = 0
#         if not __end:
#             __end = len(self.object)
#
#         l = len(__sub)
#
#         for i in range(len(self.object[__start:__end]) - l):
#             if self.object[__start:__end][i:i + l] == __sub:
#                 return i
#         else:
#             return -1
#
#     def rjust(self, width, field_char):
#         if len(self.object) >= width:
#             return self.object
#         else:
#             res = field_char * (width - len(self.object)) + self.object
#             # for i in range(width-len(self.object)):
#             #     res += field_char
#             return res
#     def replace(self , old_val , new_val , limit = None):
#         if not limit:
#             limit = len(self.object)
#         res = ''
#
#
#     def format(self, *args):
#         for i in args:
#             self.object = self.replace("{}" , i , 1)
#         return self.object
#



# 3 ta string method

# Pascal case
# class ClassName:
#     pi = 3.14
#     e = 2.72
#
#     def __init__(self, arg1, arg2, arg3):
#         self.arg1 = arg1
#         self.arg2 = arg2
#         self.arg3 = arg3
#
#     def add(self):
#         return self.arg1 + self.arg2
#


"""
json
# task 1 :
#     File(file_path) 
#         read()
#         write(data)
        
task 2:
    Student(id , fullname , username , password)
        save_to_file()
        delete_from_file(student_id)
        get_from_file(student_id)
        
task 3:
    User(name , age , balance)
        year()
        sub_balance(summ)
        add_balance(summ)            
"""
# class File:
#     def __init__(self, file_path):
#         self.file_path = file_path
#     def read(self):
#         f = open(self.file_path , "r")
#         data = f.read()
#         return data
#
#     def write(self, data):
#         file = open(self.file_path, 'w')
#         file.write(data)
#         file.close()
#
# f = File("/home/dilshod/PycharmProjects/Python_21/module_2/lesson_1/test.txt")
# f.write('Hello2')
# print(f.read())


# class A:
#     def __init__(self, a , b , c):
#         self.a = a
#         self.b = b
#         self.c = c

    # def __str__(self):
    #     return f"{self.a} {self.b} {self.c}"
    # def __repr__(self):
    #     return f"{self.a}, {self.b} ,{self.c}"


# a = A(1,2,3)
# print(a)
# print(len([a][0].a))


# class A:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def method(self,a,b):
#
#         print(a)
#         print(self.a)
#
#     def method2(self):
#         self.method2()
#
# a = A(1,2)
# a.method(3,4)
# a.method2()
# print(a.name)

# vendors = []
# class Vendor:
#     def __init__(self , id , user_id , balance):
#         self.id = id
#         self.user_id = user_id
#         self.balance = balance
#     def save(self):
#         vendors.append(self)
#
#     def delete(self,vendor_id):
#         for vendor in vendors:
#             if vendor.id == vendor_id:
#                 vendors.remove(vendor)
#     def update(self, field , new_val):
#         for vendor in vendors:
#             if vendor.id == self.id:
#                 if field == "user_id":
#                     vendor.user_id = new_val
#                 elif field == "balance":
#                     vendor.balance = new_val
#
#
#
#     def get_vendor(self , vendor_id):
#         for vendor in vendors:
#             if vendor.id == vendor_id:
#                 return vendor.__dict__
#
#     def __repr__(self):
#         return f"{self.balance}"

# v = Vendor(1 , 1 , 100000)
# v2 = Vendor(2 , 1 , 2000)
# v2.save()
# v.save()
# v.update("balance" , 50000)
# # v2.delete(1)
# print(v.get_vendor(2))
# print(vendors)

