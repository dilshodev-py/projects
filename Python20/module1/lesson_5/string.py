# a = """
# sadfs dasfsgd
# sadfs dsafgd
# dsaf adsf dasfsgd
# """
# b = "sadfs dasfsgd\n\
# sadfs dsafgd\n\
# dsaf adsf dasfsgd"
# # c = "Hello     \b\b\b\bo' world !"
#
# on = ord("A")
# c = "\101\145\154\154\157"
# """
# \t  - > tab
# \n  - > kyingi qator
# \b  - > 1 ta space kamaytiradi chap tomondan
# \000- > 8 lik sanoq sistemasidagi sonlarni belgiga o'tkazadi
# """
# print(c)


# a = "Hello "
# b = "World"
#
# print(a + b)
# print(a , b)

# format
# f"TEXT : {a}"
# print("TEXT : {} {}".format(b , a))
# print("TEXT %s" % a)

# description = "Product : {} , price : {} , term : {}"
# product = input("Product : ")
# price = input("Price : ")
# term = input("Term : ")
# print(description.format(product , price , term))
# print(f"Product : {product} , price : {price} , term : {term}")

# matn = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
# b = "simpyl"
# if b in matn:
#     print(True)
# else:
#     print(False)
# a = "hEllo WoRld . John"
# ===================== replace
# print(a[::-1].replace('l', 'x',1)[::-1])
# ===================== split
# var1 = a.rsplit('|', 1)
# print(var1)
# ['Hello   ','' , 'World']

# """1 54 78 43"""
# x,  y , c , d = map(int , input().split())

# print("|".join(a.split())) # "Hello World"


# ===================== capitalize
# print(a.capitalize())

# ===================== casefold
# print(a.casefold())

# ===================== title
# print(a.title())

# ===================== count
# print(a.count('l' , start_index , end_index ))
# print(a.count('L' , start_index , end_index ))
# print(len(a))

#  ===================== find

# print(a.find('abs', 1 , 4))

#  ===================== index

# print(a.index('abs'))
# print(10)


#  ===================== ljust
# b = '2'
# b = b.rjust(2, '0')

# print(a.index('abs'))
# print(10)


#  ===================== lower
# print(a.lower())

#  ===================== strip
# message = "|{|sa    lom||||" #
# print(message.strip('{|ml'))

#  ===================== splitlines
# message = """Hello
# world"""
# print("".join(message.splitlines(keepends=False)))
# print(message.split('\n'))

# ================= swapcase
# print(message.swapcase())

# ================= startswith
# a = "Hello world"
# print(a.startswith("Hello world"))


# ================= startswith
# a = "Hello_world.py"
# print(a.removeprefix("E"))
# print(a.strip("E"))
# print(a.removesuffix(".py"))

# =================== isascii
# print("(A".isascii())

# =================== isspace
# print("".isspace())
# on = ord("1")
# print(oct(on))
#
# print("19\61".isdecimal())
# print("19\10".isdecimal())
# print("19\61".isdigit())


# print("2".zfill(2))
# print("2".rjust(2 , '0'))

# print(type("Hello".encode().decode())) # 10 lik 01010101


# def swapcase(satr):
#     result = ''
#     for i in satr:
#         on = ord(i)
#         if 65 <= on <= 90:
#             result += chr(on + 32)
#         elif 97 <= on <=122:
#             result += chr(on - 32)
#         else:
#             result += i
#     return result


# print(swapcase("Hello"))

# def removeprefix(satr , char):
#     if satr[:len(char)] == char:
#         return satr[len(char):]
#     return satr
#
#
# print(removeprefix('Car', 'c'))


# print(chr(1000))

# print("~".isascii())

# def isascii(satr):
#     for i in satr:
#         if not 32 <= ord(i) <= 126:
#             return False
#     return True
#
#
# print(isascii('Apiuy23456()'))
# print(" ".isascii())

"""
replace     ✅
split       ✅
rsplit      ✅
join        ✅
capitalize  ✅
casefold    ✅
title       ✅
count       ✅
find        ✅
index       ✅
ljust       ✅
rjust       ✅
lower       ✅
lstrip      ✅
rstrip      ✅
rfind       ✅         
rindex      ✅
splitlines  ✅
strip       ✅
swapcase    ✅
upper       ✅
startswith  ✅
endswith    ✅
removeprefix✅
removesuffix✅
isascii     ✅
islower     ✅
isupper     ✅
istitle     ✅
isspace     ✅
isdecimal   ✅
isdigit     ✅
isnumeric   ✅
isalpha     ✅
isalnum     ✅
zfill       ✅
format      ✅
encode      ✅

"""

# def defangIPaddr(address : str) -> str:
#     return address.replace('.' , '[.]')
#
# address = "1.1.1.1"
# print(defangIPaddr(address))


def strongPasswordChecker(password: str) -> int:
    if len(password) < 6:
        motion = 6 - len(password)
    else:
        motion = 0
    c = 1
    is_lower = False
    is_upper = False
    is_number = False
    while c < len(password):
        if password[c].isalpha() and password[c-1] == password[c]:
            if motion != 0:
                pass
            else:
                motion += 1
        if password[c-1].islower():
            is_lower = True
        if password[c-1].isupper():
            is_upper = True
        if password[c-1].isdigit():
            is_number = True
        c += 1
    if len(password) >= 6 and not is_number:
        motion += 1
    if len(password) >= 6 and not is_upper:
        motion += 1
    if len(password) >= 6 and not is_lower:
        motion += 1

    return motion


print(strongPasswordChecker('aaaa123'))

