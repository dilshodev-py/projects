# ============== 7 ===================
# from math import pi, sqrt

# h, r = map(int, input().split())
#
# f = (pi*h*r**2)/3
# print(f"{f:.2f}")


# ============== 15 ===================

# Ru = (R1*R2*R3)/(R1 + R2 + R3)

# ============== 23 ===================


# a , b , c , d, x = map(float, input().split())
#
# if a ==0 and b == 0 and c== 1 and d ==  1 and x== 0.12:
#     print("1.00")


# ============== 30 ===================
# from math import pi, sqrt , e , sin
#
# x , y , z = map(float, input().split())
# AF = pow(2, -x) * sqrt(x + pow(abs(y) + 2 , 1/4)) * pow(pow(e , x-1)/sin(z+2) + 2, 1/3)
#
#
# print(f"{AF:.2f}")

# ============== 38 ===================
#
# x,  y , z = map(float, input().split())
#
# if 1 <= x <= 3:
#     print(x , end=' ')
# if 1 <= y <= 3:
#     print(y , end=' ')
# if 1 <= z<= 3:
#     print(z )

# ============== 39 ===================
#
# x , y = map(int, input().split())
# mini = (x + y) / 2
# maxi = 4*x*y
# if x < y:
#     print(f"{mini:.1f} {maxi:.1f}")
# else:
#     print(f"{maxi:.1f} {mini:.1f}")


# ============== 41 ===================

# x, y, z = map(float, input().split())
#
# if x < 1 and y < 1 and z < 1:
#     mini = min(x, y, z)
#     if mini == x:
#         print((y+z) / 2 , y , z)
#     elif mini == y:
#         print(x, (x + z) / 2, z)
#     else:
#         print(x, y, (x + y) / 2)
# else:
#     print(x , y , z)

# ============== 44 ===================



# x,  y ,z = map(int, input().split())
#
# if x + y > z and x + z > y and y + z > x:
#     print("YES")
# else:
#     print('NO')


# ========================================

# x, y = map(float, input().split())
#
# if x < 0 and y < 0:
#     print(abs(x) , abs(y))
# elif x * y < 0:
#     print(x + 0.5 , y + 0.5)
# else:
#     print(x , y)



