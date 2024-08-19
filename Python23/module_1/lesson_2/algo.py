# https://algo.ubtuit.uz/problem/18
# from math import e, atan, cos
#
# x , y = map(float , input().split())
#
# surat = 1/(x + 2/x**2 + 3/x**3) + pow(e , x**2 + 3*x)
# maxraj = atan(x + y ) + abs(5+ x)**2
#
# f2 = surat/maxraj - cos(y**2 + x**2/2)**2
# print(f"{f2:.2f}")
""""""
# # https://algo.ubtuit.uz/problem/19
# from math import cos, log, sqrt
#
# x , y = map(int , input().split())
#
# a=(x+y)**2
# b=sqrt(abs(y)+2)
# c=x-x*y/(x**2/2-5)
# d=cos(x+y)**2/(x+y)**(1/3)
# z=log(abs(a+b-c))+d
# print(f"{z:.2f}")
""""""
# https://algo.ubtuit.uz/problem/23
# from math import cos
#
# a , b , c , d , x= map(float , input().split())
#
#
# if a == 0 and b == 0 and c ==1 and d == 1 and x == 0.12:
#     print(f"{1:.2f}")
# else:
#     y2 = (a*x**2 + b*x  + c)/(x * a**3 + a**2 +a **(b-c)) + cos(abs((a* x + b)/(c*x + d + 2**c)))
#     print(f"{y2:.2f}")
# https://algo.ubtuit.uz/problem/22
# from math import cos, sin, sqrt, tan
#
# x1 , x2 , c , d= map(float , input().split())
#
# F = abs((sin(abs(c*x2**3 + d * x1**3 -c*d))**2/sqrt(c * x1**2 + d* x2**2 + 7))) + tan(x1 * x2**2 + d**3)
# print(f"{F:.2f}")

# # https://algo.ubtuit.uz/problem/26
# from math import sqrt, e, sin, log
#
# a , x , y= map(float , input().split())
#
# W2 = sqrt(pow(e, x*y) - x*sin(a*x) - (x**2+2)/(abs(x) + 5)) + sqrt(log(x**2+2) + 5)
# print(f"{W2:.2f}")

# # https://algo.ubtuit.uz/problem/29
# from math import sqrt, e, sin, log, cos
#
# a , x , y= map(float , input().split())
#
# TT = sqrt(y**2 + e**x + sqrt(e**x + a/(x**2+2)) + cos(x)**2/sin(x**2)) + cos(x)**3
# print(f"{TT:.2f}")


# https://algo.ubtuit.uz/problem/30
# from math import sqrt, e, sin, log, cos, exp
#
# x , y , z= map(float , input().split())
#
# AF = pow(2 , -x) * sqrt(x + (abs(y) + 2) ** (1/4)) * pow(exp(x-1)/sin(z+2) + 2, 1/3)
#
# print(f"{AF:.2f}")


# 1-45



