
# 4x5
# matrix = [
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5]
# ]

# print(*[i[0] for i in matrix],sep='\n')
# ===================================
# for i in matrix:
#     i[0] , i[-1] = i[-1], i[0]
# print(matrix)

# ====================================


# board = [
#     [".",".",".",".",".",".",".","."],
#     [".",".",".","p",".",".",".","."],
#     [".",".",".","R","B",".",".","p"],
#     [".",".",".",".",".",".",".","."],
#     [".",".",".","B",".",".",".","."],
#     [".",".",".","p",".",".",".","."],
#     [".",".",".",".",".",".",".","."],
#     [".",".",".",".",".",".",".","."]
# ]
# row = col = 0
# for i in range(len(board)):
#     if  'R' in board[i]:
#         row , col = i , board[i].index("R")
#         break
#
# col_list = [j for i in board for j in i[col] if j != '.']
# row_list = [i for i in board[row] if i!= '.']
# row_r_index = row_list.index('R')
# col_r_index = col_list.index('R')
# count = 0
# if  row_r_index != 0 and row_list[row_r_index-1] == 'p':
#     count += 1
# if row_r_index != len(row_list)-1 and row_list[row_r_index + 1] == 'p':
#     count += 1
# if col_r_index != len(col_list)-1 and col_list[col_r_index + 1] == 'p':
#     count += 1
# if col_r_index != 0 and col_list[col_r_index - 1] == 'p':
#     count += 1
# print(count)

"""
home_work:
    algo : 130-147
    leetcode matrix: +5
"""

# ========================== 144 ===============


# n , m = map(int, input().split())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))

# array = [sorted(list(i)) for i in list(zip(*matrix))]

# for i in list(zip(*[list(i[::-1]) for i in array])):
#     print(*i)









