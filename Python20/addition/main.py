# import time
#
# arr = list(range(1, 100000000))
# x = 99999999
# start = time.time()
# for i , v in enumerate(arr):
#     if v == x:
#         print(i)
#         break
# print(time.time() - start)


# BIG O
# O(1)
# O(N)
# O(logN)


# def binary_search(arr , x):
#     low = 0
#     high = len(arr)-1
#     mid = 0
#     c = 0
#     while low <= high:
#         c += 1
#         mid = (low + high) // 2
#         if arr[mid] > x:
#             high = mid - 1
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             print(f"Topishlar soni : {c}")
#             return mid
#     return -1
#
# arr = list(range(1 , 100000))
# x = 1
# print(binary_search(arr, x))
# import time
# from multiprocessing import Pool
# def copy_file(num):
#     with open("plan" , 'r') as f:
#         data = f.read()
#     with open(f"file{num}.txt" , "w") as f:
#         f.write(data)
#
# start = time.time()
# with Pool(20) as p:
#     p.map(copy_file , range(20))
# # for i in range(20):
# #     copy_file(i)
# print(time.time() - start)






