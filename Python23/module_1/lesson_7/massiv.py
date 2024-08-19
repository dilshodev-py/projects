"""string"""
# nums = "12345678909"
# for i in range(0,len(nums), 2):
#     print(nums[i : i+2])
#
# for i in range(0,len(nums), 3):
#     print(nums[i : i+3])
#
# for i in range(len(nums)):
#     print(nums[i: i+2])


"""
input : str_ = "234542223"
output : 2

23 34 45 54 42 22 22 23
"""
# str_ = "234542223"
# count = 0
# for i in range(len(str_)-1):
#     if str_[i] == str_[i+1]:
#         count += 1
# print(count)

"""
massiv : str , list , tuple , set , dict
list : [True, True , "123" , 12 , 0.8]

"""

# l = [True, True , "123" , 12 , 0.8]
# print(l.clear())
# print(l)
# print(id(l))
# b = l
# print(id(b))
# b.remove(12)
# print(l , b)

# fruits = []
# fruits.insert(0 , "apple")
# fruits.insert(0 , "orange")
# fruits.insert(0 , "watermelon")
# fruits.append("apple")
# fruits.append("orange")
# print(fruits)
# iterabe -> str , list , tuple , set , dict

# numbers = [1,2]
# numbers.extend(["hello"])
# print(numbers)
# 1 2 1 2 3 4 5

# numbers = "satr$ nimadir$"
# print(numbers.replace("$", ""))


# numbers = [1,2,3,4,5,5,6]
# for i in range(numbers.count(5)):
#     numbers.remove(5)
# print(numbers)
# numbers.pop(1)

# numbers = ["801", "5611", "54", "93111"]
# numbers.sort(key = lambda x : eval("+".join(x)))
# numbers.sort(key = lambda x : len(x))
# print(numbers)
# 80 93 54 56
# print(numbers.index(77))
# numbers.reverse()
# print(numbers)
# print(numbers.sort(reverse=False , key = lambda x : x[1]))
# print(numbers)

"""
clear
copy
append
insert
extend
pop
remove
index
count
reverse
sort
"""

# print(l[2])
# print(l[-1])
# print(l[::-1])
# print(l[-2:])
# print(l[1::2])
# for i in l:
#     print(i)


""" 
mutable(o'zgaruvchan)  -> list , tuple , set , dict 
immutable(o'zgarmas)   -> str , int , float , tuple , complex 
"""
# a = 1
# print(id(a))
# a += 2
# print(id(a))
# a = [1,2,3,4]
# print(id(a))
# a += [5]
# print(id(a))
#
#
# a = (1,2,3)
# print(id(a))
# a += (5,)
# print(id(a))


# names = ["John" , "Botir" , "Kamol" , "Farhod"]
# names[1] = "Suhrob"
# names[0] , names[2] = names[2] , names[0]
# print(names)

# names = ["John" , "Botir" , "Kamol" , "Farhod"]
# names = "John Botir Kamol Farhod".split()
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1


# l =  ["tail", "body", "head"]
#
# l[0] , l[-1] = l[-1] , l[0]
#
# print(l)

# def monkey_count(num):
    # result = []
    # for i in range(1 , num + 1):
    #     result.append(i)
    # return result
    # i = 1
    # while i <= num:
    #     result.append(i)
    #     i += 1
    # return result
    # return list(range(1 , num+1))

# print(monkey_count(5))
# memory management

# nums = [1, 2, 3]
# print(nums , id(nums))
#
# i = 0
# while i < len(nums):
#     nums[i] *= 2
#     i += 1
# print(nums , id(nums))
# for i in range(0 , len(nums)):
#     nums[i] = nums[i] * 2
# print(nums , id(nums))





