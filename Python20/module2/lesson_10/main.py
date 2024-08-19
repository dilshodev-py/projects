# import bcrypt
#
# salt = bcrypt.gensalt()
# hash_pw = bcrypt.hashpw('123'.encode(), salt)
# print(bcrypt.checkpw('1234'.encode(), hash_pw))


# input : 4 password

# list
#
# hash_passwords = []
#
# class Hash:
#     def save(self, value):
#         value = value.encode()
#         salt = bcrypt.gensalt()
#         hash_pw = bcrypt.hashpw(value, salt)
#         hash_passwords.append(hash_pw)
#
#
#     def check(self, value):
#         for hp in hash_passwords:
#             if bcrypt.checkpw(value.encode(), hp):
#                 return True
#         else:
#             return False
#
# Hash().save("123")
# Hash().save("222")
# Hash().save("555")
#
# print(Hash().check("565")) # True


# salt = bcrypt.gensalt()
# hash_pw = bcrypt.hashpw('123'.encode(), salt)
# print(bcrypt.checkpw('1234'.encode(), hash_pw))

# try:
#     print(1/1)
# except:
#     print("xatto chiqdi")
# print(20)
# import math
# try:
#     1/0
# except Exception as msg:
#     print(msg)


# class MyException(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     num1 = 1
#     num2 = 2
#     if num2 == 0:
#         raise ZeroDivisionError("sondi 0 qiymatiga bo'lib bulmaydi")
#     print(num1 / num2)
# except ZeroDivisionError as msg:
#     print(msg)


# try:
#     1/0
# f = open()
# f.read() # xatolik
# # code
# f.close()
# except:
#     print("xatolik")
# else:
#     print("Successful")
# finally:
#     print("finnaly")
import json


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data

    def write(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=3)


try:
    username = input(">>>")
    users = File('user.json').read()
    for user in users:
        if user.get("username") == username:
            print(user)
            break
    else:
        raise Exception("Bunda username mavjud emas")

except Exception as msg:
    print(msg)

# login register - authentication
