# def construct_submatrix(matrix, rows_to_delete, cols_to_delete):
#     rows_to_delete.sort(reverse=True)
#     cols_to_delete.sort(reverse=True)
#     for i , val in enumerate(rows_to_delete):
#         del matrix[val]
#     if matrix:
#         matrix = list(zip(*matrix))
#         for i , val in enumerate(cols_to_delete):
#             del matrix[val]
#         matrix = list(zip(*matrix))
#     return list(map(list , matrix))
#
#
#
# matrix = [[1,2], [3,2]]
# rowsToDelete = [0,2]
# columnsToDelete = [0]
# print(construct_submatrix(matrix, rowsToDelete, columnsToDelete))

#
# def get_neighbourhood(n_type, mat, coordinates):
#     result = []
#     row , col = coordinates
#     if col - 1 >= 0:
#         result.append(mat[row][col - 1])
#     if col + 1 <= len(mat[0]) - 1:
#         result.append(mat[row][col + 1])
#     if row + 1 <= len(mat) - 1:
#         result.append(mat[row+1][col])
#     if row - 1 >= 0:
#         result.append(mat[row - 1][col])
#     if n_type == "moore":
#         if col - 1 >= 0 and row - 1 >= 0:
#             result.append(mat[row-1][col-1])
#         if row - 1 >= 0:
#             result.append(mat[row-1][col+1])
#         if col + 1 <= len(mat[0])-1:
#             result.append(mat[row+1][col+1])
#         if col - 1 >= 0:
#             result.append(mat[row + 1][col -1])
#
#     return result
#
#
#
#
#
#
#
#
#
# mat = [
#     [0, 1, 2, 3, 4],
#     [5, 6, 7, 8, 9],
#     [10, 11, 12, 13, 14],
#     [15, 16, 17, 18, 19],
#     [20, 21, 22, 23, 24]
# ]
#
# print(get_neighbourhood("moore", mat, (0 , 4)))


# def ritual(n: int) -> int:
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append((i + 1) * (j + 1))
#         matrix.append(row*2)
#     print(matrix)
#
# ritual(4)

# [
#     [1, 2, 3, 1, 2, 3],
#     [2, 4, 6, 2, 4, 6],
#     [3, 6, 9, 3, 6, 9]



def points(games):
    result = 0
    # for i in games:
    #     x,  y = map(int , i.split(":"))
    #     if x > y:
    #         result += 3
    #     elif x == y:
    #         result += 1
    return sum([3 if int(i[0]) > int(i[2]) else 1 if int(i[0]) == int(i[-1]) else 0  for i in games])

# games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
# print(points(games))



# def flip(d, a):
#     return sorted(a) if d == "R" else sorted(a, reverse = True)


# print(flip('R', [3, 2, 1, 2]))

# l = [3, 2, 1, 2]
# print(sorted(l, reverse=True))





