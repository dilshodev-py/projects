

"""memory"""
# a = 6
# b = 6

# print(id(a))
# print(id(b))
# a += 1
# print(id(a))
# print(id(b))

# print(hash("123"))

# hash  - > orqaga qaytmidi
# shifr - > orqaga qaytarib buladi
# company -> database dasturchi
# bcrypt


# print(all([True, [1,2,3], True]))
# print(any([False, True, True]))
# print(chr(65))
# print(ord('\u0440'))
# print(eval("1+(7*10)/10"))
# print(isinstance("ty", int))
# print(range(1, 101, 2)) # lazy
# print(sum([1,2,3,5,6]))


# name = "John"
# s = slice(1 , 4, 2)
# print(name[s])
# print(oct(10))
# print(hex(10))
# print(int('12', 8))
# print(oct(198))
# print(int("306" , 8))
# print(bin(10))
# print(hex(10))
# ========================================

# def my_function():
#     print("Hello world")
#
# my_function()

# def add_nums(num1 , num2 = 0):  # argument
#     return num1 + num2
#
# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
# result = add_nums(10) # parametr
# print(result)


# def print_info(name , age , at_work):
#     return f"Name : {name} , age: {age} , at_work : {at_work}"

# print(print_info(age=25 , name="John"  , at_work="Google"))


# group_by("123sadf23456adsfdg")
# output:
#     raqam : 5
#     belgi : 4
# print(48 <= ord(i) <= 57)

# def group_by(satr):
#     raqam = 0
#     belgi = 0
#     for i in satr:
#         if 48 <= ord(i) <= 57:
#             raqam += 1
#         else:
#             belgi += 1
#     print(f"raqam : {raqam}\nbelgi : {belgi}")


# str_ = "123sadf23456adsfdg"
# print(group_by(str_))


# *args , **kwargs

# def any_arg(**kwargs):
#     print(kwargs['n1'])
#
# any_arg(n1 = 1 , n2 = 2 , n3 = 3)

# def any_arg(*args):
#     c = 1
#     for i in args:
#         c *= i
#     return c

# any_arg(1,2,3,4,5, 80 , 56 , 42)














