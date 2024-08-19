# monkeytype
# windows(graf) -> linux(backend)
# ============ string ===============
a = "botirjon"
a = "o'glon"
a = 'o"glon'
a = 'o\'glon'
a = """botirjon"""
a = '''botirjon'''
#  -------------------------------------
# a = 100
# b = 20
# result = a + b
# print(a , '+' , b , '=' , result)
# print(f"{a} + {b} = {result}")
# 40 + 20  = 60


# a = "age"
# a = "name\n\n\n\n\nage"
# print(a)


# f""
# '\t' # 4 TA SPACE
# '\n' # new line
# '\r' # after remove
# r""
#
# =========================================
# name = "Botirjon"
# age = "25"
# num = int(input()) # 3

# print(name)
# for i in range(num):
#     print('\n' , end='')
# print(age)
# ==========================================
# f""
# "" + "" + ""
# print("a b")


# s = "   s      salom                  "
# 21
# 23


# print(s.title())
# print(s.casefold())
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.find("e"))
# print(s.index("t"))

# =====================================
# print(s.replace("HI" , "salom"))
# print(s.replace("HI" , "salom"))
# print(s.encode()[0])
# print(s[0])
# print(s.lstrip(' s'))
# print(s.rstrip(' s'))
#
# nums = [1,2,3,4,5,6,7]
# nums = list(map(str , nums))
# print("|".join(nums))
#
# b = '1123456'
# print(b.center(8 , "0"))
# print(b.count("1"))
# print(b.expandtabs(1))
# print(b.partition('3'))

# d = {65 : 97}
# month = """A Hello"""
# print(month.rjust(2, "0"))
# print(month.splitlines(False))
# print(month.swapcase())
# print(month.translate(d))



# file_name = ["revision.py" , "main.cpp" , "tasks.txt"]
# name = "botir"
# print(name.startswith("Boti"))
#
# for i in file_name:
#     if i.endswith('.py'):
#         print(i)

nimadir = "a "
print(nimadir.isspace())


# month = "4"
# print(month.zfill(2))
# print(month.rjust(2,"0"))

"""
title  ✅
encode ✅
replace ✅
split ✅
rsplit ✅
lstrip ✅
join ✅
capitalize ✅
casefold ✅
center ✅
count ✅
expandtabs ✅
find ✅
partition  ✅
index ✅
ljust  ✅
lower ✅
lstrip ✅
rfind ✅
rindex ✅
rjust  ✅
rstrip ✅
rpartition ✅
splitlines  ✅
strip ✅
swapcase  ✅
translate ✅
upper ✅
startswith  ✅
endswith ✅
removeprefix ✅
removesuffix ✅
isascii ✅
islower ✅
isupper ✅
istitle ✅
isspace ✅
isdecimal ✅
isdigit ✅
isnumeric ✅
isalpha ✅
isalnum ✅
isidentifier ✅ (*&^
zfill ✅
format ✅ 
format_map  ✅
maketrans ✅
"""

taklifoma = """
Assalomu alaykum {name}
manzil : sergili , munis restoran
sizni taklif qilamiz oshga !
"""
# print(taklifoma.format_map({"name": "Ism"}))
# print(taklifoma.format(name = "Ism"))

# "" + ""


# f""
#
# names = ["Botir" , "Kamol" , "Rustam"]
# for name in names:
#
# n = "Hi"
# swap = n.maketrans('H' , "B")
# print(n.translate(swap))

# ======================================


def word_count(input_string):
    return input_string.count("word")

print(word_count("word word word salom"))




