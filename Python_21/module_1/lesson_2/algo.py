"""algo - 10"""
# x = int(input())
# y = x*365*24*60*60//1000
# print(y)


"""algo - 11"""


# n = int(input())
# print(n*(n+1)//2)
# """algo - 12"""
# m = int(input())
# g=9.8
# print(f"{m * g:.2f}")


"""algo - 13"""


# m , a = map(int , input().split())
# F = m*a
# print(F)


"""algo - 14"""


# U , R = map(int , input().split())
# I = U/R
# print(f"{I:.3f}")


"""algo - 15"""


# R1 , R2 , R3 = map(int , input().split())
# summ = 1/R1 + 1/R2 + 1/R3
# Rum = 1/summ
# print(f"{Rum:.2f}")


"""algo - 18"""


# from math import e, atan, cos, exp
# x , y = map(float , input().split())
# surat = 1/(x + 2/x**2 + 3/x**3) + exp(x**2 + 3 * x)
# maxraj = atan(x + y) + abs(5 + x)**2
# f2 = surat/maxraj - cos(y**2+ x**2/2)**2
# print(f"{f2:.2f}")


"""algo - 19"""


# x , y = map(int , input().split())
# z = logs(abs((x + y)**2 + sqrt(abs(y) + 2) - (x - ((x*y)/(x**2/2 - 5)))))  + cos(x + y)**2/(x + y)**(1/3)
# print(f"{z:.2f}")


"""algo - 22"""


# from math import logs, e, sqrt, cos, sin, tan
#
# x1 , x2 , c , d = map(float, input().split())
#
# F = abs((sin(abs(c*x2**3 + d*x1**3 - c * d))**2)/(sqrt(c*x1**2 + d*x2**2 + 7))) + tan(x1*x2**2 + d**3)
# print(f"{F:.2f}")


"""algo - 23"""


# from math import logs, e, sqrt, cos, sin, tan
# a, b, c, d, x = map(float, input().split())
# if a == 0 and b == 0 and c == 1 and d == 1 and x ==0.12:
#     print(f"{1:.2f}")
# else:
#     y2 = (a*x**2 + b * x + c) / (x * a**3 + a**2 + a**(b-c)) + cos(abs((a*x + b)/(c*x + d + 2**c)))
#     print(f"{y2:.2f}")


"""algo - 28"""


# from math import logs, e, sqrt, cos, sin, tan, log10
# a, x = map(float, input().split())
# BB1 = x * sin(x/2+x/3+x/4) + (log10(x**2-2) + 3**a)/(cos(x+ 3) * sin(x + 3) + 8)
# print(f"{BB1:.2f}")


"""algo - 29"""
# True if cond else False

# from math import logs, e, sqrt, cos, sin, tan, log10
# a, x , y = map(float, input().split())
# TT = sqrt(y**2 + e**x + sqrt(e**x + a / (x**2+2)) + cos(x)**2/sin(x**2)) + cos(x)**3
# print(f"{TT:.2f}")