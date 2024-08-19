# 3
# 38 39 41
# 1 2

# len_ = int(input())
# massiv = list(map(int , input().split()))
# k , l = map(int , input().split())
#
# tmp = massiv[k-1:l]
# print(f"{sum(tmp) / len(tmp):.1f}")


# len_ = int(input())
# massiv = list(map(int , input().split()))
# m = max(massiv)
# for i in massiv:
#     print(f"{i/m:.2f}" , end=' ')


# len_ = int(input())
# massiv = list(map(int , input().split()))
# K , M = map(int , input().split())
# r = 1
# for i in massiv:
#     if K == i or M == i:
#         r *= i
#
# print(r)

# len_ = int(input())
# massiv = list(map(int , input().split()))
# toq = 1
# juft = 0
# for i in massiv[::2]:
#     toq *= i
# for i in massiv[1::2]:
#     juft += i
# print(f"{toq/juft:.2f}")

# len_ = int(input())
# massiv = list(map(int , input().split()))
#
# toq = [i for i in massiv if i % 2 == 1]
# print(f"{sum(toq)/len(toq)+0.0001:.2f}")


# 10
# 14 51 -83 42 85 -77 91 70 -98 54
# 50 99

# len_ = int(input())
# massiv = map(int , input().split())
# x , y = map(int , input().split())
# c = 0
# for i in massiv:
#     if not x <= i <= y:
#         c += 1
# print(c)

"""
6
29 50 -14 4 -14 -56
3

"""

# len_ = int(input())
# massiv = list(map(int , input().split()))
# k =  int(input())
# maxi = max(massiv)
# k_element = massiv[k-1]
# index = 0
# for i in massiv:
#     if maxi == i:
#         massiv[index] = k_element
#     index += 1
# massiv[k-1] = maxi
# print(*massiv)

# for i in range(len(massiv)-1):
#     massiv[-1]
# from math import log
#
# len_ = int(input())
# massiv = list(map(int , input().split()))
# tmp = log(sum(massiv)/len(massiv))
# index = 0
# for i in massiv:
#     if i < 0:
#         massiv[index] = tmp
#     index += 1
#
# for i in massiv:
#     print(f"{i:.2f}" , end = ' ')


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
