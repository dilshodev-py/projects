from math import log2
def binary_search(array, value):
    L, H = 0, len(array) - 1
    count = 0
    while L <= H:
        count += 1
        M = (L + H) // 2
        if array[M] == value:
            print(count)
            return M
        elif value > array[M]:
            L = M + 1
        elif value < array[M]:
            H = M - 1
    print(count)
    return -1


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


def bubble_sort(array):
    swapped = True
    i = 0
    count = 0
    while swapped:
        count += 1
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        i += 1
    print(count)
    return array


# print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23))
# print(selection_sort([22, 54, 8, 120, 163, 23, 38, 56, 72, 91]))
print(bubble_sort([5, 8, 12, 16, 23, 38, 56, 72, 91, 2]))
