# a = "LeEeetcode"
# Leetcode

# b = "HhboLl"
# bo
# replace

# for i in b:
#     b = b.replace(i + i.swapcase(), "")
# print(b)



# ifoda = "(1 + 2 * (7 - ((10/6))) - ((((90 - 5)))))"
# 5
# count = 0
# maxi = 0
# for i in ifoda:
#     if i == "(":
#         count += 1
#         maxi = max(count , maxi)
#     elif i == ")":
#         count -= 1
# print(maxi)

# l = ["$56.a$df$()76", "$89$.786ag8"]
# [5676 , 897868]
# for i in range(len(l)):
#     tmp = ""
#     for j in l[i]:
#         if j.isdigit():
#             tmp += j
#     l[i] = "$" + tmp[:-2] + "." + tmp[-2:]
# print(l)



# trello
#
# yuklash    prosecc     end     test





# ["$56.76" , "$8978.68"]
# a = "8790"
# a= a[:-2] + "." + a[-2:]
# print(a)

# iterable[str , list , dict , tuple , set]

# iterator , generator

# iter()
# next()
# function -> generator




# print(type(iter_massiv))
# print(list(iter_massiv)[-1])


# for i in range(len(l)):
#     print(l[i])

 # iterable
# iter_massiv = iter([1,2,3])
# while True:
#     try:
#         i = next(iter_massiv)
#         # logic
#     except:
#         break

# for i in iter_massiv:
#     print(i)

# class MyIterable:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         n = self.index
#         self.index += 1
#         return self.iterable[n]
#     def __len__(self):
#         c = 0
#         for i in self.iterable:
#             c += 1
#         return c

# l = list([1,2,3,4])
# l = iter(l)
# print(next(l))
# l = iter(MyIterable([1, 2, 3, 4]))
# print(l.__next__())
# print(next(l))

# iterator generoator emas
# generator bu itarotor
# generator

# def my_generate(iterable):
#     for i in iterable:
#         yield i


# data structure -> iterator, generator , list node
# ListNode
# print(my_generate([1, 2, 3, 4, 5]))


def my_map(function , iterable):
    for i in iterable:
        yield function(i)

range(10, 100)

for i in my_map(lambda x : x**3, [1, 2, 3]):
    print(i)



# filter(function , iterable)
# for i in filter(lambda x: x % 2 == 0, [1,2,3,4]):
#     print(i)


# for i in gener_random_number():
#     print(i)

# generator
# my_range(start , end , step)

# a = lambda x : x
# def f(function):
#     return function(10)
# print(f(a))

def my_range(*args):
    start = 0
    step = 1
    if len(args) == 1:
        end = args[0]
    if len(args) == 2:
        start = args[0]
        end = args[1]
    if len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]

    while start < end:
        yield start
        start += step


print(list(my_range(10)))
print(list(range(10)))






