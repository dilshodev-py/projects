""""""
import random

"""
iterable -> list , set , tuple , str , dict
iterator -> memory , __iter__
generator -> memory , function(yield) , 
    list(map(function , iterable)     [function1 , function2]
    filter(function , iterable)
    range(start , end , step)
    next()
"""

# print(list(map(lambda x : x**2 , [1,2,3])))
# print(tuple(filter(lambda x : x % 2 == 1 , [1,2,3])))


# 1 task
# def cycle():
#     while True:
#         yield random.randint(1, 100)
#
# for i in cycle():
#     print(i)

"2 task"
# def fibonachi(max_):
#     a, b = 1, 1
#     if max_ == 1:
#         yield a
#     elif max_ == 2:
#         yield a
#         yield b
#     else:
#         yield 1
#         yield 1
#         c = 2
#         while c < max_:
#             yield a + b
#             a, b = b, a + b
#             c += 1
#
# for i in fibonachi(3):
#     print(i)

"4 task"

# def random_password(max_):
#     from string import ascii_letters, digits, punctuation
#     random_pass = ""
#     for j in range(1 , max_+1):
#         for i in range(16):
#             random_pass += random.choice(ascii_letters + digits + punctuation)
#         yield f"password {j} -> {random_pass}"
#         random_pass = ""
#
# for i in random_password(10):
#     print(i)


"task 6"

# def double(iterable):
#     for i in iterable:
#         yield i*2
#
# for i in double([1,2,3,4]):
#     print(i)

# nums = [0,0,0,1,2,3,4] # memory
# print(id(nums) , nums)
# nums.remove(4)
# print(id(nums) , nums)


# nums = [0,0,0,1,1,1,2,2,3,3,4]
# for i in nums:
#     for _ in range(nums.count(i)-1):
#         nums.remove(i)
# print(nums)












