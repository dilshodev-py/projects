"""string"""

# a = "o'" \
#     "ret" \
#     "fert" \
#     "ret" \
#     ""
# print(a)
# a = 'o\'' \
#     'fdsg' \
#     'fsdgf' \
#     'fsdgfh' \
#     'gfdgfhg' \
#     ''
# print(a)
# a = """adsf
# sfdg
# adsfg
# srdgf
# """
# print(a)
# a = '''dsfg
# dfsg
# dfsg
# dfg
# '''
# "\n \t"
# a = "he\tllo"
# print(a)

# num1 = 10
# num2 = 20
# print(f"{num1} + {num2} = {num1 + num2}")
# print(num1 , "+" , num2 , "=" ,num1 + num2)
# # 10 + 20 = 30
# a = "{} + {} = {}".format(num1 , num2 , num1 + num2)
# print(a)

# string methods

a = "Hello World"
print(a.title())
print(a.upper())
print(a.lower())
print(a.lower())
print(a.capitalize())
print(a.count("l" , len(a)-4))
print(a.index("l",3))
print(a.casefold())
print(a.casefold())
print(a.startswith("ell"))
print(a.endswith("rld"))
print(a.swapcase())
print(a.find("p"))
# print(a.index("p"))
print(a.replace("p", "1" , 1))
# print(a.decode())
print("1 2 3 4 6".split())
print("1,2,3,4,6".split(sep = ",",maxsplit= 1))
print("1,2,3,4,6".rsplit(sep = ",",maxsplit= 1))
month = "4"
print(month.rjust(2 , '0'))
print(month.ljust(10 , '0'))
a = "11"
print(a.center(4 , "0"))
print("|".join(["1" , "2" , "3"]))



message = "                           mes       sage           "
print(message.strip(" m e"))
print(message.rstrip("m e"))
print(message.lstrip())
a = "algo.py"
print(a.removesuffix(".py"))
print(a.removeprefix("m"))

"""
title ✅
count ✅
index ✅
capitalize ✅
casefold ✅
upper ✅
lower ✅
swapcase ✅
find ✅
startswith  ✅
replace ✅
encode ✅
split ✅
rsplit ✅
center ✅
ljust ✅
lstrip ✅
rfind ✅
rindex ✅
rjust ✅
rstrip ✅
strip ✅
removeprefix  ✅
removesuffix ✅
isascii
islower
join    ✅ 
isupper
istitle
isspace
isdecimal
isdigit
isnumeric
isalpha
isalnum
isidentifier 
isprintable
zfill
format ✅
"""


# 147-164

s = input()

print(s.count("A"))
print(s.count("Y"))









