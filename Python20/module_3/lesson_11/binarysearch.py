from math import log2


# print(log2(100_000_000_000))
def binary_search(arr , key , low , high):
    c = 0
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            print(c)
            return mid
        elif arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid-1
        c += 1

arr = range(1,1_000_000)
key = 500_000
print(binary_search(arr, key, 0, len(arr) - 1))

def bubble_sort(arr) -> list:
    j = 0
    swapped = True
    while swapped:
        i = 0
        swapped = False
        while i < len(arr)-1-j:
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
                swapped = True
            i += 1
        j += 1
    return arr

def selection_sort(arr) -> list:
    pos = 0
    l = len(arr)
    while pos < l:
        mid_index = pos
        j = pos + 1
        while j < l:
            if arr[mid_index] > arr[j]:
                mid_index = j
            j += 1
        arr[pos] , arr[mid_index] = arr[mid_index] ,arr[pos]
        pos += 1
    return arr

def insertion_sort(arr) -> list:
    i = 1
    while i < len(arr):
        j = i
        while arr[j-1] > arr[j] and j - 1 >= 0:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j -= 1
        i+=1
    return arr

arr = [67, 37, 1, 34, 78, 87, 45, 23]
print(insertion_sort(arr))

