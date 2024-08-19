# ======== 148 ============

# s = input().split()
# for i in s:
#     # if i[0] == 'A':
#     #     print(i)
#     if i.startswith('Ab'):
#         print(i)

# ======== 149 ============
# s = input().split()
# count = 0
# result_worlds = ''
# for i in s:
#     if i.endswith('NA'):
#         count += 1
#         result_worlds += f"{i} "
# print(count, "\n" , result_worlds)

# ======== 150 ============


# s = input().split()
#
# for i in s:
#     if "info" in i.lower():
#         print(i , end=' ')

# ======== 153 ============
# s = input().split()
# pos = int(input())

# result = ""
# for p , word in enumerate(s ,1):
#     if p == pos:
#         result += 'TATU '
#         continue
#     result += f"{word} "
# print(result)

# ======= 2-usul ===========
# s[pos-1] = "TATU"
# print(*s)

from string import ascii_lowercase

# taklifnoma = "Assalomu alaykum {name} sizni shu yaxshi {v} kunimizga taklif qilamiz"

# names = ["Botir", "Bobur", "Qodir"]
# for i in names:
#     print(taklifnoma.format(name=i , v="value" ))
#     print(taklifnoma.format_map({"name": i, "v": "value"}))

# names = ["Botir" , "Navruz" , "Kamron" , 1]
# print(" ".join(map(str ,names)))
# result = ""
# for name in names:
#     result += f"{name} "
# print(result)
# "Botir|Navruz|Kamron"

# print("1".ljust(10, '.'))
# print("1".rjust(10, '.'))
# year = 2024
# month = 12
# day = 1
# print(f"{year}-{str(month).rjust(2, '0')}-{str(day).rjust(2, '0')}")

# 2024-06-01

# print("aHello".removeprefix('aH'))
# print("aHello.py".removesuffix(".py"))
#
# print("abca".find("a", 1 , 3))

# print("a b c d".split(" " , 1))
# print("a b c d".rsplit(" ", 1))
# sher = """
# wqergthyqwdefrgth
# qwergth
# wefrgthy
# wdefrgth
# """
# print(sher.splitlines())
# print("HellO".swapcase())
# print("6".zfill(10))

# leetcode 500+


# s = "hello"
# print(sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)))
#
# summ = 0
# for i in range(len(s)-1): summ += abs(ord(s[i]) - ord(s[i+1]))
# print(summ)

# s = "abc"
# t = "bac"
# summ = 0
# for i in range(len(s)):
#     summ += abs(i-t.find(s[i]))
# print(summ)


"""
Home work:
    algo       : 1-45 , 60-100 , 147-172
    leetcode   : 10+
    self study : list and method 
"""











