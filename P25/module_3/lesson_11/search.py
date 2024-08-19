# linear search
# l = range(1, 10000)
# count = 0
# for i in l:
#     if i == 1000:
#         print(count)
#         break
#     count += 1
from math import log2

# Big (O)
# O(1)
# O(log2(n))
# O(n)
# O(n**2)
# O(2**n)

# ================== BINARY SEARCH ============

# massiv = list(range(1, 10**6))
# L = 0
# H = len(massiv) - 1
# find = 987643
# count = 0
# while L <= H:
#     count += 1
#     M = (L + H) // 2
#     if massiv[M] == find:
#         print(f"Urunishlar soni {count}")
#         print(M)
#         break
#     if massiv[M] < find:
#         L = M + 1
#     else:
#         H = M - 1
# else:
#     print(-1)


# ====================== BUBBLE SORT ==========================

# l = [54,12]
#
#
#
# def bubble_sort(l):
#     for i in range(len(l)):
#         swapped = False
#         for j in range(len(l) - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j] , l[j + 1] = l[j + 1], l[j]
#                 swapped = True
#         if not swapped:
#             break
#     return l
#
# def selection_sort(l):
#     for i in range(len(l)):
#         min_index = i
#         for j in range(i + 1, len(l)):
#             if l[j] < l[min_index]:
#                 min_index = j
#         l[i] , l[min_index] = l[min_index], l[i]
#     return l
#
#
# def test_sort(l):
#     for i in range(1,len(l)):
#         j = i - 1
#         while j>=0 and l[j] > l[j + 1]:
#             l[j], l[j+1] = l[j + 1] , l[j]
#             j -= 1
#     return l
#
#
# print(test_sort(l))






