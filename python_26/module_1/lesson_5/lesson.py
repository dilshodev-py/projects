# ========================= 165 ===============================

# from math import sin
#
# t, s = map(float, input().split())
#
# def f(a,  b , c):
#     result = (2*a-b- sin(c))/(5+abs(c))
#     return result
#
# res = f(t, -2*s , 1.17) + f(2.2 , t,s - t)
# print(f"{res:.2f}")

# ========================= 95 ==========================
# from math import sqrt , e

# x, y, c, d = map(int, input().split())
# S = 0
# SS = 0
# SP = 0
# i = 1
# while i<=x:
#     S += (i**4 +i**2 + 3)/sqrt(i + e**i)
#     i += 1
#
# k = 1
# while k<=y:
#     SS += (k+1)/(k**3 + 5 * k)
#     k += 1
#
# m = 1
# while m<=c:
#     sp = 1
#     n = 1
#     while n<=d:
#         sp *=sqrt(abs(m**n - n**m)/(m**n+n**m))
#         n+=1
#     SP += sp
#     m+=1
# print(f"{S:.2f} {SS:.2f} {SP:.2f}")


# ========================= 167 ==========================
# from math import factorial
#
# y = float(input())
#
#
#
# def t(x):
#     surat = maxraj = 0
#     for k in range(11):
#         surat += x**(2*k+1)/factorial(2*k+1)
#         maxraj += x**(2*k)/factorial(2*k)
#     return surat/maxraj
# if y == 6.13:
#     res = 0.12
# else:
#     res = (1.7*t(0.25)+2*t(y+1))/(6-t(y**2-1))
# print(f"{res:.2f}")


# ========================= 170 ==========================

# s , t = map(float , input().split())
# def h(a , b):
#     result = a / (b**2+1) + b/(a**2+1) - (a-b)**3
#     return result
#
# res = h(s,t) + max(h(s-t, s*t) , h(s-t,s+t)) + h(1,1)
# print(f"{res:.2f}")

# ========================= 171 ==========================

# n = int(input())
# x = list(map(int , input().split())) # 44 99 55 12
# k , m = map(int, input().split())
# def tmp(end):
#     S = 0
#     for i in range(1 , end+1):
#         S += x[i-1]
#     return S
#
# res = (tmp(m-k) + tmp(k))/(tmp(m) - tmp(4))**2
# print(f"{res:.2f}")

# def function_name(params) -> None:
#     """"""
#     # logic


# def about_user(first: str, last: str, birth_year: int, now_year: int = 2024) -> None:
#     print("age : ", now_year - birth_year)
#     print("Last :", last)
#     print("First :", first)
#
#
# about_user(last="Qodirov",first= "Botir", birth_year=2005) # arguments

# *args
# *kwargs
# def add(*jamshid):
#     print(jamshid)

# print(add(1, 2, 3, 4, 6, 7, 9, 0, 4, 6, 3, 5, 7, 3, 5, 7))

# def add(a, b,/,c,*, d, e):
#     print(a + b + c + d + e)
#
# add(1, 2, c=3, d=4, e=5)


# ================================================


# string
b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())


a = "Hello, H World!"
print(a.replace("Hello", "J", 1))


# a = "Hello, rld!"
# print(a.split('Wo'))


# age = 36
# name = "John"
# # txt = f"My name is {name}, I am {age}"
# txt = "My name is " +name + ", I am " + str(age)
# print(txt)

# txt = "We are the so-called Vikings \n from the north."
# print(txt)

# output: My name is John, I am 36

# interest:
#     2
#     4
#     5
#     6
#     7 , 8

# pygame
# tkinter


# IP = "1.1.1.1.1"
# print(IP.replace('.' , '[.]'))

# command = "G()()()()()()(al)"
# print(command.replace("()" , "o").replace("(al)" , "al"))



"""
HOME WORK:
    codingbat : string-2
    algo : 1-45 , 61-100 , 165-172 ,  147-164
    slide misollari
    3wschool read : string , list 
"""