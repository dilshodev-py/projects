# decorator -> function boyitib beradi


# def a(permission_list):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if file_write:
#                 with open("test.txt" , 'a') as f:
#                     f.write(f"{result}\n")
#             else:
#                 return result
#         return wrapper
#     return inner
# # test.txt
# @a(file_write=True)
# def my_function(name):
#     return "Hello " + name

# @a(file_write=True)
# def function2(x, y):
#     return x, y
# # function2(x=10, y=20)
# print(my_function("John"))

# def is_permission(permission_list: list[str]):
#     def inner(func):
#         def wrapper(*args , **kwargs: dict):
#             if kwargs.get("user").get("role") in permission_list:
#                 return func(*args)
#             else:
#                 return "Permission denied"
#         return wrapper
#     return inner
#
# @is_permission(["ADMIN" , "TEACHER"])
# def add(x, y):
#     return x + y
# # @is_permission(["ACTOR"])
# # def div(x , y):
# #     return x / y
#
#
#
# user1 = {
#     "id": 1,
#     "fullname": "John",
#     "role": "ADMIN"
# }
# user2 = {
#     "id": 2,
#     "fullname": "Carl",
#     "role": "STUDENT"
# }
#
# user3 = {
#     "id": 3,
#     "fullname": "Lili",
#     "role": "TEACHER"
# }
#
# user4 = {
#     "id": 4,
#     "fullname": "Flip",
#     "role": "ACTOR"
# }

# print(add(10, 30, user = user1)) # 40
# print(add( 1, 3, user = user2)) # permission denied
# print(add( 1, 6, user = user3)) # 7
# print(add( 1, 6, user = user4)) # permission denied

# email , logging

# leetcode , email

# register
#     fullname
#     email
#     password
# Email code >>> 3456789

# users
#     reklama
#     vakansiya







