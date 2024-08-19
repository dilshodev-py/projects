# https://algo.ubtuit.uz/problem/77

# from math import sin, cos
#
# a , b , c , d = map(int , input().split())
# h = 2
# x = c
# S = 0
#
# while x <= d:
#     S += pow((sin(a*x) + b**(2*c))/(b**2 + cos(x)**2) , 1/3) - sin(x**2)/(a*b)
#     x += h
#
# print(f"{S:.2f}")


# https://algo.ubtuit.uz/problem/62

# from math import sin
# n = int(input())
# c = 1
# S = 0
# while c <= n:
#     S += pow(-1 , c-1) * (sin(c**c)/(2**c))
#     c += 1
# print(f"{S:.2f}")

# https://algo.ubtuit.uz/problem/63
# from math import factorial
#
# n = int(input())
# c = 1
# S = 0
#
# while c <= n:
#     S += pow(-1 , c-1)/factorial(2*c-1)
#     c += 1
# print(f"{S:.4f}")


# https://algo.ubtuit.uz/problem/92
# from math import cos, log , e
#
# x , y , a , b = map(int , input().split())
#
# S , P , SP = 0 , 1  , 0
# i , k , l  = 1 , 1 , 1
#
# while l <= x:
#     S += (l**2+2*l)/(l**3+l*cos(l)**2 + 1)
#     l += 1
#
# while i <= y:
#     P *= (i**2+1)/(pow(i , 3/i) + 2)
#     i += 1
#
# i=1
#
# while i <=a:
#     sp = 1
#     while k <= b:
#         sp *= log((k**i + pow(k,1/i)) / (k**3  +pow(i , 1/k)),e)
#         k += 1
#     SP += sp
#     i += 1
#     k = 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")





