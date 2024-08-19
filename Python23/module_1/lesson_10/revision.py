"""Revision"""
""" matrix
[   col
    [1,2,3], # row 0
    [4,5,6]  # row 1
]
row   qatorni o'zi
col   uztuning o'zi
i     qatorni indexi
j     ustunning indexi
"""
# matrix = [
#     [10,4,3],
#     [8,3,9],
#     [25,23,0]
# ]


# for j in range(len(matrix[0])):
#     for i in range(len(matrix)):
#         print(matrix[i][j] , end = ' ')
#     print()





# 10 8 25
# 4 3 23
# 3 9 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print((i,j) , end= ' , ')
#     print()

# for row in matrix:
#     for col in row:
#         print(col , end = ' ')
#     print()
# matrix = []
# n = int(input()) # 4
# tmp = list(range(1 , n*n+1))
# print(tmp)
# for i in range(n): # i=2
#     matrix.append(tmp[i*n:i*n+n])
# print(matrix)

# case: 3
# nxn
# [[1,2,3],
# [4,5,6],
# [7,8,9]]

"""matrix"""
# matrix = []
# n , m = map(int , input().split())
# for i in range(n):
#     matrix.append(list(map(int , input().split())))
#
# maxi = matrix[0][0]
# mini = matrix[0][0]
# for col in list(zip(*matrix)):
#     print(sum(col), end = ' ')
#     maxi = max(max(col) , maxi)
#     mini = min(min(col) , mini)
# print()
# print(maxi , mini)

# https://algo.ubtuit.uz/problem/132
# matrix = []
# l = int(input())
# massiv = list(map(int , input().split()))
# n , m = map(int , input().split())
#
# massiv += [0]*(n * m - l)
# for i in range(n):
#     matrix.append(massiv[i*m:i*m+m])
#
# for i in matrix:
#     print(*i)

# https://algo.ubtuit.uz/problem/134
# matrix = []
# n , m = map(int , input().split())
# for _ in range(n+1):
#     matrix.append(list(map(int , input().split())))
#
#
# for i in sorted(matrix, key=lambda row: row[0], reverse=True):
#     print(*i)




# https://algo.ubtuit.uz/problem/136
# matrix = []
# n , m = map(int , input().split())
# for i in range(n):
#     matrix.append(list(map(int , input().split())))
# k = int(input())
#
# for row in matrix:
#     row.pop(k-1)
#     print(*row)

# https://algo.ubtuit.uz/problem/138
# n , m = map(int , input().split())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int , input().split())))
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] < 0:
#             col_index = j
#             row_index = i
#             break
#
# for row in matrix:
#     row.pop(col_index)
# matrix.pop(row_index)
#
# for i in matrix:
#     print(*i)

# https://algo.ubtuit.uz/problem/140

# algorithm

# matrix1 = []
# matrix2 = []
# n , m = map(int , input().split())
# for i in range(n):
#     matrix1.append(list(map(int , input().split())))
#
# x , y = map(int , input().split())
# for i in range(x):
#     matrix2.append(list(map(int , input().split())))
#
# matrix = []
# for row in matrix1:
#     l = []
#     for col in zip(*matrix2):
#         S = 0
#         for i in range(len(row)):
#             S += row[i]*col[i]
#         l.append(S)
#     matrix.append(l)
#
# for i in matrix:
#     print(*i)


# https://algo.ubtuit.uz/problem/144



# matrix = []
# n , m = map(int , input().split())
# for i in range(n):
#     matrix.append(list(map(int , input().split())))
#
# new_mat = []
# for col in zip(*matrix):
#     new_mat.append(sorted(col , reverse=True))
#
# for row in zip(*new_mat):
#     print(*row)



# new_matrix = []
# for i in range(m):
#     l = []
#     for row in matrix:
#         l.append(row[i])
#     l.sort(reverse=True)
#     new_matrix.append(l)
#
# for i in range(n):
#     for j in range(len(new_matrix)):
#         print(new_matrix[j][i] , end = ' ')
#     print()

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]
# print(list(zip(*list(zip(*matrix)))))


# accounts = [[1,2,3],[1,3,2,1]]
# summ = 0
# maxi = sum(accounts[0])
# for row in accounts:
#     for col in row:
#         summ = summ + col
#     if maxi < summ:
#         maxi = summ
#     summ = 0
# print(maxi)




# accounts = [[1,2,3],[1,3,2,1]]
# print(sum(sorted(accounts , key = sum)[-1]))

# input :
matrix = [
    ["#", "#", "-", "#"],
    ["#", "-", "#", "-"],
    ["-", "#", "-", "#"],
    ["#", "#", "-", "-"],
    ["-", "-", "#", "-"],
    ["#", "-", "-", "-"]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '#':
            matrix[i][j] = '-'
            tmp = -1
            while matrix[tmp][j] == '#':
                tmp -= 1
            matrix[tmp][j] = '#'

print(*matrix, sep = '\n')






# output
"""
[
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["#", "#", "#", "-"],
    ["#", "#", "#", "#"]
]
"""




















