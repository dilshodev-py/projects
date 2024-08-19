""""""

"""
if / elif / else     :  yes
string slice         :  
operators:
    mantiqiy         : and  , not , or
    arifmetik        : + , - , * , / , // , ** , %   - yes
    taqoslash        : < , > , != , == , >= , <=  , is
    o'zlashtirish    : += , -= , *= , /= , %= , //= , = , **=
    bitwise operator : & , | , ^ , << , >>, ~
bin()                :
int()                : 
f"{9.20456 : .2f}"                        
"""
# if cond:
#     body
#
# elif cond:
#     body
# else:
#     body


# print(~-5)

# print(int(10101))

# while (cond):
#     body
#     break
# else:
#     finally

# i = 1
# while i <= 100:
#     i += 1
#     if i == 55:
#         break
#     print(i)
# else:
#     print("finally")

# cheksiz tskil


# i = 65
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 65
# while i <= 100:
#     print(i)
#     i += 2
# start : 13


# start, end = map(int, input().split())
# while start <= end:
#     if start % 5 == 0:
#         print(start)
#     start += 1
# from math import sin , factorialn

# n , i , s = int(input()) , 1 , 0
# while i <= n:
#     s, i = s + sin(i)/2**i , i + 1
# print(s)

# ctrl + 2*space
# from math import factorial
# n , x , i , s = int(input()) , int(input()) , 1, 0
# while i <= n:
#     s += pow(-1, i-1)*pow(x , 2*i-1)/factorial(2*i-1)
#     i += 1
# print(s)
"""
iterable:
    str
    list
    set
    tuple
"""

# for variable in iterable:
#     # body
# else:
#     print("finally")

# for i in range(20, 1 , 1):
#     if i == 55:
#         continue
#     print(i)
# else:
#     print("Finally")

# start , end = int(input()) , int(input())
# for i in range(start + start%2, end+1 , 2):
#     print(i)

# print(list(range(20, 1 , -1)))


# ===========================================
# from math import sqrt , e

# x, y, c, d = map(int, input().split())
# S = 0
# i = 1
# while i<=x:
#     S += (pow(i,4) + pow(i, 2) + 3)/sqrt(i + e**i)
#     i += 1
#
# SP = 0
# for m in range(1 , c+1):
#     sp = 1
#     for n in range(1 , d+1):
#         sp *= sqrt(abs(pow(m, n) - pow(n ,m))/(pow(m,n) + pow(n , m)))
#     SP += sp

# print(f"{SP:.2f}")

