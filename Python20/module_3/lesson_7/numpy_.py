import numpy as np

# massiv = [1, 2, 3]

# arr = np.array([42])
#
# print(arr[0]) # index
# print(type(arr), arr)

matrix = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [1, 2, 3],
        [4, 5, 9]
    ]
]
# 2 x 3
arr = np.array(matrix)
print(arr[1, -1, 2])
print(arr.ndim)
