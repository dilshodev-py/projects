"""sikl"""
# massiv -> str , list , set , tuple , dict
from math import sin, factorial

"""
for (int i = 0 ; i < 10 ; i++){
    logic
}
"""
# massiv1 = [1,2 , "hi" , 4]
# massiv2 = {1,2 , "hi" , 4}
# name = "Botirjon"
# for item in massiv1:
#     print(item, end=" ")


# while cond:
#     # logic
#     pass



# i = 0
# for i in range(start , end):
#     print(i)
#     # continue
#     # break
#     print(10)
# else:
#     print("Finally item")

# numbers = "1,,,,,,2,3,4,5,6"
#
# count = 0
# for item in numbers:
#     if item == ",":
#         count += 1
# else:
#     print(count)


# numbers = 1111
# summ = 0
# for i in str(numbers):
#     summ += int(i)
# print(summ)


# n = int(input())
# S = 0
# i = 1
# while i <= n:
#     S += 1/i
#     i += 1
# print(S)


start = 10
end = 40

# for i in range(start , end + 1):
#     if i % 2 == 0:
#         print(i)
#
#
# while start <= end:
#     if start % 2 == 0:
#         print(start)
#     start += 1


# https://algo.ubtuit.uz/problem/61

# n = int(input())
# S = 0
# i =1
# while i <= n:
#     S += sin(i)/(2**i)
#     i += 1
# print(f"{S:.2f}")

# https://algo.ubtuit.uz/problem/70
# from math import factorial
# n , x = map(int , input().split())
#
# S = 0
# i = 1
# while i <= n:
#     S += pow(-1 , i-1)*pow(x, 2*i - 1)/factorial(2*i-1)
#     i += 1
# print(f"{S:.3f}")
# https://algo.ubtuit.uz/problem/80

# from math import *
# a = int(input())
# S = 0
# x = 0
# h = 0.5
# while x <= 10:
#     S += a*cos(x) - sin(x**2)
#     x +=h
# print(f"{S:.2f}")

# https://algo.ubtuit.uz/problem/91
# from math import *
# a , b , c , d = map(int , input().split())
#
#
# S , P , SP = 0 , 1 , 0
# m , k , i = 1 , 1 , 1
#
# while m <=a:
#     S += (3*m**3 + 4 * m + 5)/(m**3 + log(m))
#     m += 1
#
#
# while k <= b:
#     P *= k/(k**3+7*k + 5)
#     k += 1
#
# while i <= c:
#     sp = 1
#     m = 1
#     while m <= d:
#         sp *= (log(i) + m**i)/(m**i)
#         m += 1
#     SP += sp
#     i += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")


