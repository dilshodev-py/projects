"""
''
""
"""

"""
format
f"{}"
"{} {} {}".format(1 , 2 , 3)
"Salom %s" % ("Botir")
"""

a = "hello John"
b = a.encode("UTF-8")
print(b[2])

# replace
print(a.replace("l", "p", 1))

# split
print(len(a.split("|")))

# join
print(" ".join(map(str , ["1" , 2 , '3']))) # 1 2 3

# capitalize
print(a.capitalize())


# casefold
print(a.casefold())


# title
print(a.title())


# center
a = "3123"
print(a.center(4))


# count
print(a.count("3"))


# find
print(a.find("31",1))


# partition
print(a.partition('12'))


# index
# a = "3123"
# print(a.index("9"))


# ljust , rjust
# month = "4"
# day = "1"
# year = "2023"
# print(f"{year}-{month.rjust(2, '0')}-{day.rjust(2, '0')}")


# strip
# a = "       hehllo world       "
# print(a.strip(" h"))


# a = "2  3   5 6 3"
# print(a.rpartition("3"))

# a = """aBc"""
# print(a.splitlines())

# swapcase
# a = "01"
# print(a.zfill(3))


"""
encode    ✅
replace   ✅
split     ✅
rsplit    ✅
join      ✅
capitalize✅
casefold  ✅
title     ✅
center    ✅
count     ✅
find      ✅
partition ✅
index     ✅
ljust     ✅
lower     ✅
strip     ✅
lstrip    ✅
rstrip    ✅
rfind     ✅ 
rindex    ✅
rjust     ✅
rpartition✅
splitlines✅
swapcase  ✅ 
upper     ✅
startswith✅
endswith  ✅
removeprefix✅
removesuffix✅
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
zfill   ✅
format  ✅
"""






