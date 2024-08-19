# abs()    # module
# bin()    # 2 lik
# bool()   # True , False , type cast
# max()    # eng katta son topadi
# min()
# float()  # type cast
# input()  # consoldan qiymat qabul qilish
# pow()    # **
# range()  #
# len()    # uzunlik topiladi
# type()   # type aniqlash
# round()  # yaxlitlash
# print()  # chop etish
# map()    # type cast
# str()    # type cast
# sum()    # yig'indi
# id()     # memory address

# and
# print(all([True , True , True]))
# or
# print(any([False , False , True]))
# print(chr(65))
# print(ord("A"))
# revision

code = """
a = 5
b = 20
print(a + b)
"""
# compile_var = compile(code , ' ', mode='exec')
# exec(compile_var)
# print(hex(10)) # 16 lik
# print(oct(10)) # 8 lik
# print(bin(10)) # 2 lik
# print(int('12', 8))
# hash()
# shifr()

# slice_ = slice(1,  5)
# print("123456789"[slice_])
""" built-in functions
all()
any()
chr()
ord()
compile()
exec()
hex()
oct()
hash()
slice()
enumerate()
isinstance()
"""


# for index , value in enumerate("Hello"):
#     print(index , value)

# a = True
# if isinstance(a , int):
#     print(a)

# 20:30

# def hello_world() -> None:
#     '''Hello world degan textni print qilib beradigan funksiya'''
#     print("Hello world")
#
#
# print(hello_world())


# def add(num1: int, num2: int , step = 1) -> int:
#     result = num1 + num2
#     return result
#
#
# print(add(10, 20))


# def clone_range(start:int , end:int=10 , step:int = 1) -> None:
#     """range funksiyasini o'xshash varianti"""
#     while start < end:
#         print(start)
#         start += step
#
# clone_range(1)

# lambda params : logic

# add = lambda num1, num2: num1 + num2
# print(add(1, 20))
# print(add(1, 20))
# print(add(1, 20))
# print(add(1, 20))
# print(add(1, 20))
# print(add(1, 20))

# def pow_clone(a , b):
#     return a ** b

# pow = lambda a , b : a ** b


# print(pow(2, 5))

# def factorial(num : int) -> int:
#     return 1 if num == 0 else num*factorial(num-1)
# def factorial(num: int) -> int:
#     if num == 0:
#         return 1
#     tmp = 1
#     for i in range(1, num + 1):
#         tmp *= i
#     return tmp
#
#
# print(factorial(5))

# def reverse_word(word : str) -> str:
#     return word[::-1]
#
# print((lambda word: word[::-1])("salom"))
# print(reverse_word("salom"))


# def is_palindrome(text: str) -> bool:
#     return text == text[::-1]

# print(is_palindrome("arra"))
# print((lambda text : text == text[::-1])("word"))

# def count_vowels_consonants(word: str, unli=0) -> None:
#     for i in word:
#         unli += i in "aioueAIOUE"
#     print("unli :", unli, "\nundosh :", len(word) - unli)


# def count_vowels_consonants(word: str) -> None:
#     print(f"unli : {(unli_count := sum([i in 'aioueAIOUE' for i in word]))} \nundosh : {len(word) - unli_count}")
#
#
# count_vowels_consonants("salom")

"""
console:
    unli : 2
    undosh : 3
"""
