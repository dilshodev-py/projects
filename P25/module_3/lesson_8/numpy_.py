# import numpy as np
#
# arr = np.array([42])
#
# print(arr.ndim)


# =============================

import numpy as np
#
# list_ = [
#     [
#         [1,2],
#         [34,65]
#     ],
#     [
#         [65,90],
#         [67,8]
#     ]
# ]
# arr = np.array(list_)
#
# print(arr[1,1,0])

# ===================================

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 2])

import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# row , col = arr.shape

# arr = np.array([1, 2, 3, 4], ndmin=5)
#
# print(arr)
# print('shape of array :', arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(2,3,2)
#
# print(newarr)


# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = arr.reshape(2, 3)
#
# print(newarr.base)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8 ,5, 6, 7, 8 ])
#
# newarr = arr.reshape(2, 2,-1)
#
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(2, 3, 2)
#
# print(newarr)


# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# for x in np.nditer(arr):
#   print(x)

# arr = np.array([1, 2, 3])
#
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)

# arr = np.array([[1, 2], [3, 4], [5, 6]])
#
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)


# arr1 = np.array([[1, 2], [3, 4]])
#
# arr2 = np.array([[5, 6], [7, 8]])
#
# arr = np.concatenate((arr1, arr2))
#
# print(arr)
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.dstack((arr1, arr2))
#
# print(arr)

# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr, 5)
#
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 5)
#
# print(x)
#
# arr = np.array([6, 7, 8, 9])
#
# x = np.searchsorted(arr, 7)
#
# print(x)

# arr = np.array([[3, 2, 4], [5, 0, 1]])
#
# print(np.sort(arr))

# from numpy import random
#
# x = int(random.rand()*10**6)
#
# print(x)

# x=random.randint(100, size=(3,5))
#
# print(x)


