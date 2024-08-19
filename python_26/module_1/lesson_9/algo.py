from math import sin

# ================ https://algo.ubtuit.uz/problem/102
# n = int(input())
# massiv = list(map(int , input().split()))
# a, b = map(int , input().split())
#
# mini = min(massiv)
# for p , v in enumerate(massiv , 1):
#     if a <= p <= b:
#         v = v/mini + 0.00001
#     print(f"{v:.1f}" , end=" ")


# ================ https://algo.ubtuit.uz/problem/114

# input()
# massiv = map(int, input().split())
#
# result = 1
# for i in massiv:
#     if not i % 2 or not i % 5:
#         result *= i
# print(f"{sin(result):.2f}")

# ================ https://algo.ubtuit.uz/problem/116


# input()
# massiv = list(map(int , input().split()))
#
# maxi = max(massiv)
# for i in massiv:
#     result = i / maxi + 0.000001
#     print(f"{result:.2f}" , end = " ")

# ================ https://algo.ubtuit.uz/problem/118

# input()
# massiv = list(map(int , input().split()))
# result = []
# for i in massiv:
#     if i % 2:
#         result.append(i)
#
# print(f"{sum(result)/len(result)+0.00001:.2f}")

# ================ https://algo.ubtuit.uz/problem/123

# input()
# massiv = list(map(int , input().split()))
# juft_position = 0
# toq_value = 0
# summa = sum(massiv[1::2])
# for pos , value in enumerate(massiv,1):
#     if value % 2 and value > 0:
#         value = value / summa + 0.00001
#     print(f"{value:.2f}" , end = " ")


# ================ https://algo.ubtuit.uz/problem/124


# input()
# massiv = list(map(int , input().split()))
# k = int(input())
#
# maxi = max(massiv)
# for pos , value in enumerate(massiv,1):
#     if maxi == value:
#         print(massiv[k-1] , end = ' ')
#     elif pos == k:
#         print(maxi , end = " ")
#     else:
#         print(value, end= " ")


# a = [1,2,3]
# a =  a + list("1234567")
# print(a)

# print([i for i in range(1, 101) if not i % 5])

# 1 : 20

# ["1-toq" , "2-juft" , "3-toq", ....]
# print([f"{i}-juft" if i % 2 == 0 else f"{i}-toq" for i in range(1, 21)])


# massiv = ["ajdavwe" , "ajwefjkhebw" , "dasvkhs"]
# print(sum(i.count("a") for i in massiv))
# print(sum(j == "a" for i in massiv for j in i))
# 3

# emails = ["botir@gmail.com@gmail.com" , "komil@gmail.com" , "Lider$gmail.com"]
# print(sum(i.count("@gmail.com") == 1 and i.endswith("@gmail.com") for i in emails))

















