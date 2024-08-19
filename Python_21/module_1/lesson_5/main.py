# a = """
# string ->
#     split() , f"" , '' , "" , """""" , '''''',
#     isupper() , islower() , isdigit() , isalnum() , isalpha()
#     slice[start : end : step]    [::-1]
#     \n , \t , r
# """
# # print(a)
#
# # a = "Hello \n \t"
# # name = "Botir"
# # print(a + ' ' + name)
# #
# # 'o\'rdak'
# # "o'rdak"
# # """o'rdak"""
# """
# string ->
#     split() , f"" , '' , "" , """""" , '''''',
#     isupper() , islower() , isdigit() , isalnum() , isalpha()
#     slice[start : end : step]    [::-1]
#     \n , \t , r
# """
# # a = "Hello"
# # # print(ord("A"))
# # # print(chr(65))
# # # chr()
# #
# # print("A" < "-")
# #
# # K , k = 0 , 0
# # for i in a:
#
#     # if 65 <= ord(i) <= 90:
#     #     K += 1
#     # elif 97 <= ord(i) <= 122:
#     #     k += 1
#
# #     if "A" <= i <= "Z":
# #         K += 1
# #     elif "a" <= i <= 'z':
# #         k += 1
# # print(f"K : {K}\nk : {k}")

a = "hel lo WorWld"
"title()"
print(a.title())

"split()"
print(a.split())


"count"
print(a.count("lo"))

"index"
print(a.index("W"))



"find"
print(a.find("p" , 8))

"upper"
print(a.upper())

"swapcase"
print(a.swapcase())


"startswith"
print(a.startswith("hel lo"))

b = "truck.py"
"endswith"
print(b.endswith('.py'))


y = "hello"
print(y.isascii())


u = "           "
"isspace"
print(u.isspace())

a = "Lorem yana nimadir"
"replace()"
print(a.replace(" ", "continue"))

a = "hello"
"encode"
print(a.encode().decode())


h = "1 2 3 4"
"rsplit"
print(h.rsplit(" ", 1))

h = ["1" , "2" , "3" , "4"]
"join"
"1 2 3 4"
print(" ".join(h).split())




a = "lorem nimadir. kimdir"
print(a.capitalize())

a = "lorem nimadir. KIMDIR"
"casefold"
print(a.casefold())


month = "2"
"ljust"
print(month.rjust(2, '0'))



a = "p            spalom  p nimadir             p"
print(a.lstrip(' ps'))

a ="""s dasfghjh dfsghj sdgfhgj sfdgfthygj. dsfghj
b
c
"""
print(a.splitlines(True))

a = "pymain.py"
"removeprefix"
print(a.removeprefix('py'))

month = "2"
"zfill"
print(month.zfill(2))

"""
title    ✅
split    ✅
count    ✅
index    ✅
find     ✅
upper    ✅
swapcase ✅
lower    ✅
startswith ✅
endswith ✅
isascii  ✅
islower  ✅
isupper  ✅ 
istitle  ✅
isspace  ✅
isdecimal ✅
isdigit ✅
isnumeric ✅
isalpha ✅
isalnum ✅
isidentifier ✅
replace      ✅
encode       ✅
rsplit       ✅
join         ✅
capitalize   ✅
casefold     ✅
ljust        ✅
rjust        ✅
lstrip       ✅
rstrip       ✅
strip        ✅
rfind        ✅
rindex       ✅
splitlines   ✅
removeprefix ✅
removesuffix ✅
zfill        ✅ 
format       ✅
"""
"hello" # helo

"""aaabbaacc""" # a3b2a2c2

# a = "Hurmatli : {} sizni shu faxriy yorliq bilan tahdirlimiz"

# faxrli yorliq

# name = ["ahror" , "kamol" , "jamol"]
# for i in name:
#     print(a.format(i))

"================   FORMAT ======================="
# "{}".format()                                         1
# f""                                                   2
# print("name : %s , %s , %s" % ("1" , "2" , "3"))      3




