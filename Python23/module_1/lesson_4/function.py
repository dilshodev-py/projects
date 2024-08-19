""""""

"""
c++

int function_name(int a ,int b){
    logic
    return val
}

PYTHON
def function_name(a : str , b : int):
    logic
    return val
"""

"""
id()
print()
input()
len()
abs()
all()
bin()
bool()
chr()
ord()
eval()
hex()
id()

# ===============================
hash()
isinstance()
oct()
map()
compile()
exec()
min()
max()
sum()
zip()
"""


# print(ord("A"))
# print(chr(0), end = " ")

# i = 0
# while i <= 87:
#     print(chr(i) , end = " ")
#     i += 1

# for i in range(0 , 88):
# print(chr(i) , end = " ")


# print(all([True , True , True]))
# print(any([False , False , False]))

# print(ascii("Альф"))
# print("1".isascii())  # 1-122

# def add(num1, num2):
#     summ = num1 + num2
#     return summ
#
#
# print(add(num2=20, num1=10))


# def make_fullname(name , last_name):
#     a = name , last_name
#     return a
# print(make_fullname(last_name="Qodirov", name="Jamshid"))


# a = 1        #, 2, 3, 4, 5, 6, 7.0, True, "123"
# print(type(a))

# packing - yig'ish
# unpacking - yoyish
# a , b , c  = 1, 2 , 3 # unpacking
# a = 1,2,3,4,5,6 # packing
# print(type(a))


# def division(num1 , num2):
#     return num1 / num2
# n1 = int(input("Num1 : "))
# n2 = int(input("Num2 : "))
# print(division(n1, n2))

# def pow(value, power):
#     result = value ** power
#     return result

# ctrl + alt + L
# print(pow(8, 2))


# def factorial(num: int):
#     # i = 1
#     P = 1
#     for i in range(1 , num + 1):
#         P *= i
#     # while i <= num:
#     #     P *= i
#     #     i += 1
#     return P

# print(factorial(5))
# args , kwargs


a = lambda x , i , o , p : x + i + o + p
print(a(1,1,1,1))

# b = lambda x : "Juft" if x % 2 == 0 else "Toq"
# print(b(17))
