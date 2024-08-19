"""https://algo.ubtuit.uz/problem/102"""

# n = int(input())
# massiv = list(map(int , input().split()))
# a , b = map(int , input().split())
#
# mini = min(massiv)
#
# massiv[a-1:b] = [i / mini + 0.00001 for i in massiv[a-1:b]]
# for i in massiv:
#     print(f"{i:.1f}" , end = " ")


# print(f"{8.25+0.00001:.1f}")


# a = [i/2 for i in range(1, 100)]
# print(a)

"""https://algo.ubtuit.uz/problem/105"""
# n = int(input())
# massiv = list(map(int , input().split()))
# a , b = map(int , input().split())
# massiv[a-1:b] = []
# i = 0
# l = []
# while i < len(massiv):
#     if not a-1 <= i < b:
#         l.append(massiv[i])
#     i += 1
# print(f"{sum(massiv) / len(massiv):.2f}")

"""https://algo.ubtuit.uz/problem/103"""
# n = int(input())
# massiv = list(map(int , input().split()))
# a , b = map(int , input().split())
#
# l = massiv[a-1:b]
# print(f"{sum(l) / len(l):.1f}")

"""https://algo.ubtuit.uz/problem/110"""

# n = int(input())
# m = list(map(int , input().split()))
# K , M = map(int , input().split())
# i = K*m.count(K)
# j = M*m.count(M)
# print((i if i else 1) * (j if j else 1))

"""https://algo.ubtuit.uz/problem/114"""
# from math import sin
#
# n = int(input())
# m = list(map(int , input().split()))
# p = 1
# for i in m:
#     if i % 2 == 0 or i % 5 == 0:
#         p*= i
# print(f"{sin(p):.2f}")

"""https://algo.ubtuit.uz/problem/116"""
# n = int(input())
# m = list(map(int , input().split()))
#
# maxi = max(m)
# for i in m:
#     print(f"{i / maxi+0.00001:.2f}", end = ' ')


# l = [1,2,3,4,5,6]
# for i in l:
#     print(i)
#
# for i in range(len(l)):
#     print(l[i])


"""https://algo.ubtuit.uz/problem/123"""

# n = int(input())
# m = list(map(int , input().split()))

# summ = sum(m[1::2]) # Juft o'rindagi sonlar yig'indisi
# l = []
# for i in m:
#     if i > 0 and i % 2 == 1:
#         l.append(f"{i / summ:.2f}")
#         continue
#     l.append(f"{i:.2f}")
# print(*l)

"""https://algo.ubtuit.uz/problem/127"""

# n = int(input())
# m = list(map(int , input().split()))
#
# mini_kv = min(m)**2
# for i in range(len(m)):
#     if m[i] < 0:
#         m[i] = mini_kv
# print(*m)

# nums = [0,2,1,5,3,4]
# l = []
# print(nums)
# for i in nums:
#     l.append(nums[i])
# print(l)

# nums = [1,2,3,1,1,3]
# c = 0
# for i in range(len(nums)):
#     for j in nums[i+1:]:
#         if nums[i] == j:
#             c += 1
# print(c)

# nums = [1,2,3,1,1,3]
# print(sum(nums[1::2]) / sum(nums[::2]))


nums = [2,5,1,3,4,7]
n = 3

l1 = nums[:n]
l2 = nums[n:]

# l = []
# for i in range(n):
#     l.append(l1[i])
#     l.append(l2[i])
# print(l)

# for i in range(1, n+1):
#     l1.insert(i , l2[i-1])
# print(l1)












