"""FUNCTION -> def """

# def add(num1 : int , num2 : int , num3 : int) -> int:
#     result = num1 + num2
#     return result
#
# a = [10, 20 , 30]
# print(add(*a))

# def user_print(fullname : str , age : int , now_year: int = 2023):
#     print(f"Fullname : {fullname}\nAge : {age}\nNow year : {now_year}")
#
#
# fullname = input("Fullname : ")
# age = int(input("Age : "))
# now_year = input("Now year [default:2023] :")
# if not now_year.isdigit():
#     now_year  = 2023
# else:
#     now_year = int(now_year)
#
# user_print(fullname , age , now_year)

# def user_print(fullname : str , age : int , now_year: int = 2023):
#     print(f"Fullname : {fullname}\nAge : {age}\nNow year : {now_year}")
#
# user_print(age=24 , fullname="Botir")


# def test(*args , **kwargs):
#     print(args , kwargs)

# test(1 , 2, 3 , name = "Botirjon" , age = 25)


# def test(a, b,/, c,*, d ):
#     print()
# test(1 , 2 , c = 3 ,d =  4)


# ================= factorial =================

# def factorial(num):
#     P = 1
#     i = 1
#     while i<= num:
#         P *= i
#         i += 1
#     return P
#
#
# print(factorial(0)) # 120

# ================= reverse_words =================

# def reverse_words(word):
#     return word[::-1]


# print(reverse_words("Hello")) # olleH

# ================= is_palindrome =================

# def is_palindrome(word):
#     return word == word[::-1]
#
# print(is_palindrome("ikki")) # True
# print(is_palindrome("key")) # False

# ================= is_palindrome =================

# def count_vowels_consonants(word):
#     # version 1
#     # i , unli , undosh = 0 , 0 ,  0
#     # while i < len(word):
#     #     if word[i] in "aeiou":
#     #         unli += 1
#     #     else :
#     #         undosh += 1
#     #     i += 1
#     # return f"Unli : {unli} Undosh : {undosh}"
#     unli , undosh = 0 , 0
#     for i in word:
#         if i in "aioueAIOUE":
#             unli += 1
#         else:
#             undosh += 1
#     return f"Unli : {unli} Undosh : {undosh}"

# print(count_vowels_consonants("hello")) # f"Unli : {} Undosh : {}"
# print(count_vowels_consonants("key"))   # "Unli : 1 Undosh : 2

"""a , e , i, o , u"""


# print("Ka" in "Kamol")


# for i in range(0 , len("hello")):
#     print("hello"[i])



