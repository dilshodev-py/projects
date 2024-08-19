# https://algo.ubtuit.uz/problem/131


# n , m = map(int , input().split())
# matrix = []
# for i in range(n):
#     row = list(map(int , input().split()))
#     matrix.append(row)
#
# maxi = float("-inf")
# mini = float("inf")
# for i in range(m):
#     summ = 0
#     for j in range(n):
#         summ += matrix[j][i]
#         maxi = max(matrix[j][i] , maxi)
#         mini = min(matrix[j][i] , mini)
#     print(summ, end= " ")
# print()
# print(maxi , mini)


# https://algo.ubtuit.uz/problem/133


# n = int(input())
# matrix1 = []
# matrix2 = []
# for i in range(n):
#     row = list(map(int , input().split()))
#     matrix1.append(row)
#
# for i in range(n):
#     row = list(map(int , input().split()))
#     matrix2.append(row)
#
# for i in range(n):
#     print(*(matrix1[i]+matrix2[i]))

# n , m = map(int , input().split())
# matrix = []
# for i in range(n+1):
#     row = list(map(int , input().split()))
#     matrix.append(row)
#
# matrix.sort(key=lambda x: x[0], reverse=True)
# for i in matrix:
#     print(*i)
#
# n = int(input())
# matrix = []
# for i in range(n):
#     row = list(map(int , input().split()))
#     matrix.append(row)
#
# maxi = float("-inf")
# mini = float("inf")
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             maxi = max(maxi ,matrix[i][j])
#         if i +j == n - 1:
#             mini = min(mini , matrix[i][j])
# print(maxi , mini)


# n , m = map(int , input().split())
# matrix1 = []
# for  i in range(n):
#     row = list(map(int , input().split()))
#     matrix1.append(row)
#
# x , y = map(int , input().split())
# matrix2 = []
# for  i in range(x):
#     row = list(map(int , input().split()))
#     matrix2.append(row)
#
# result = []
# for row1 in matrix1:
#     row = []
#     for i in range(y):
#         summ = 0
#         for j in range(m):
#             summ += row1[j] * matrix2[j][i]
#         row.append(summ)
#     result.append(row)
#
# print(result)
from math import inf

# n ,m = map(int , input().split())
# matrix = []
# for i in range(n):
#     row = list(map(int , input().split()))
#     matrix.append(row)
#
# new_row = []
# for j in range(m):
#     summ = 0
#     for i in range(n):
#         summ += matrix[i][j]
#     new_row.append(summ)
# matrix.append(new_row)
#
# for i in matrix:
#     print(*i)

#
# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int  ,input().split())))
#
# result = []
# for index, row in enumerate(matrix):
#     result += row[index:]
#
# print(*result)
# print(max(result) , min(result))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# n , m = len(matrix) , len(matrix[0])
#
# for row in matrix:
#     print(*row, end =" ")
#     P = 1
#     for col in row:
#         P *= col
#     print(P)
"""
1 2 3 10 
4 5 6 8 
7 8 9 11 
60 960 5544
"""


# matrix = [
#     [1, 2, 3, 10],
#     [4, 5, 6, 8],
#     [7, 8, 9, 11],
# ]
#
# n, m = len(matrix), len(matrix[0])
# lis=[]
# for row in matrix :
#     p=1
#     for col in row :
#         p*=col
#     lis.append(p)
# matrix.append(lis)
# for i in matrix:
#     print(*i)


#
# r = []
# for j in range(m):
#     summ = 0
#     for i in range(n):
#         summ += matrix[i][j]
#     r.append(summ)
#
# matrix.append(r)
# for i in matrix:
#     print(i)


# def only_one(*args):
#     true_c = args.count(True)
#     if true_c == 1:
#         return True
#     return False
#
#
#
# only_one() # False
# only_one(True, False, False) # True
# only_one(True, False, False, True) # False
# only_one(False, False, False, False) # False


# def main_diagonal_product(mat):
#     P = 1
#     for i , row in enumerate(mat):
#         P *= row[i]
#     print(P)
#
#
# main_diagonal_product([[1, 0], [0, 1]])
# main_diagonal_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# [[1, 0], [0, 1]] should return 1
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] should return 45


# def switch_gravity(lst):
#     row_l = len(lst)
#     col_l = len(lst[0])
#     for i in range(row_l):
#         for j in range(col_l):
#             if lst[i][j] == '#':
#                 lst[i][j] = '-'
#                 tmp = row_l-1
#                 while lst[tmp][j] == "#":
#                     tmp -= 1
#                 lst[tmp][j] = '#'
#     return lst


# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "#", "-", "-"],
#   ["-", "#", "-", "-"],
#   ["-", "#", "#", "-"]
# ])

# def bin_rota(arr):
#     r = []
#     print(id(r))
#     for index , val in enumerate(arr):
#         if index % 2 == 0:
#             r = r + val
#             print(id(r))
#         else:
#             r =r + val[::-1]
#             print(id(r))
#     return r



# mat = [["Stefan", "Raj",    "Marie"],
#   ["Alexa",  "Amy",    "Edward"],
#   ["Liz",    "Claire", "Juan"],
#   ["Dee",    "Luke",   "Katie"] ]
# bin_rota(mat)
