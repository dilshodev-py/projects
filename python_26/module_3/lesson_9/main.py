# Binary Search
import sys


# def binary_search(data:list, target: int):
#     l , h = 0, len(data)-1
#     m = int((l+h)/2)
#     i = 0
#     while l<=h:
#         i+= 1
#         f = data[m]
#         if f == target:
#             print("Urunishlar soni :" , i)
#             return m
#         elif f>target:
#             h = m-1
#         else:
#             l = m+1
#         m = int((l+h)/2)
#     return None

# l = list(range(1,10000000))
# print(binary_search(l,999999))


# def selection_sort(l : list):
#     for i in range(len(l)):
#         min = i
#         for j in range(i, len(l)):
#             if l[min] > l[j]:
#                 min = j
#         l[i] , l[min] = l[min] , l[i]
#     return l
#
#
# data =  [41,34,2,56,7,90,12,15,45]
# print(selection_sort(data))


# def bubble_sort(array):
#     swapped = True
#     i = 0
#     c = 0
#     while swapped:
#         swapped = False
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 swapped = True
#                 array[j] , array[j+1] = array[j+1] , array[j]
#             c += 1
#         print(c)
#         c = 0
#         if not swapped:
#             break
#
#         i += 1
#     return array
# data =  [41,34,2,56,7,90,12,15,45]
# print(bubble_sort(data))




def insertion_sort(array):
    for i in range(1,len(array)):
        j = i-1
        val = array[i]
        while j >= 0 and val < array[j]:
            array[j+1] =  array[j]
            j -= 1
        array[j+1] = val
    return array

data =  [41,34,2,56,7,90,12,15,45]
print(insertion_sort(data))



# 1 ... 1000

# https://t.me/p_26_bot?start=1
# https://t.me/p_26_bot?start=2
# https://t.me/p_26_bot?start=3
#
# ...

# QR code
# save to pdf







