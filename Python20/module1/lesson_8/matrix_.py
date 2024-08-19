# matrix  = [
#     #COL0
#     [1,2,3], # ROW 0
#     [4,5,6], # ROW 1
#     [7,8,9]  # ROW 2
# ]

# for row in matrix:
#     for col in row:
#         print(col, end = ' ')
#     print()







# matrix  = [
#     #COL0
#     [1,2,3,0], # ROW 0   -> 6
#     [4,5,6,0], # ROW 1   -> 4
#     [7,8,9,0]  # ROW 2   -> 24
#
# ]

# row_n = len(matrix)
# col_n = len(matrix[0])
# for i in range(row_n):
#     for j in range(col_n):
#         print(f"({i},{j})",end = " ")
#     print()




# (0,0)  (0,1) (0,2)
# (1,0)  (1,1) (1,2)
# (2,0)  (2,1) (2,2)


# matrix = [
#     # COL0
#     [1, 2, 3, 0],  # ROW 0   -> 6
#     [4, 5, 6, 0],  # ROW 1   -> 4
#     [4, 5, 6, 0],  # ROW 1   -> 4
#     [7, 8, 9, 0]  # ROW 2   -> 24
# ]
#
# summ = sum(matrix[0]) + sum(matrix[-1])
# for i in range(1, len(matrix)-1):
#     summ += matrix[i][0] + matrix[i][-1]
# print(summ)

# matrix = [[1, 2, 3],[4, 5, 6],[4, 5, 6]]
# summ = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if i == j or i+j == len(matrix[0])-1:
#             summ += matrix[i][j]
# print(summ)


# n , m = map(int , input().split())
# matrix = []
# maxi = float("-inf")
# mini = float("inf")
#
# for _ in range(n):
#     row = list(map(int , input().split()))
#     matrix.append(row)
#
# for row in matrix:
#     print(sum(row), end = " ")
#     maxi = max(max(row) , maxi)
#     mini = min(min(row) , mini)
# print()
# print(maxi , mini)


# 13
# 51 55 0 20 59 -17 22 38 -53 53 88 -91 61
# 4 5

len_ = int(input())
massiv = list(map(int , input().split()))
n , m = map(int , input().split())

massiv += [0]*(n*m-len(massiv))

matrix = []
for i in range(n):
    row = massiv[i*m: i*m+m]
    print(row)
    matrix.append(row)
print(matrix)


















