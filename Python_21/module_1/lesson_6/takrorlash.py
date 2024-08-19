"""
lambda
ord()
chr()
string method
    find(obj, start , end)        3
    index(obj , start , end)      3
    split( sep, max_sep)          2
    rsplit(sep , max_sep)         2
    swapcase()                    0
    upper()                       0
    lower()                       0
    startswith(obj:str)           1
    endswith(obj:str)             1
    'sep'.join(iterable:str|list|set|dict)  1
    title()                       0
    capitalize()                  0
    zfill(max_width)              1
    isdigit()                     0
    isupper()                     1
    strip(obj)                    1
    rstrip(obj)                   1
    lstrip(obj)                   1
    "{}  {}"format(arg1 , arg2 , arg3)    inf
    isspace()                     0
    isalnum()                     0
    isnumber()                    0
    replace(old_val:str , new_val:str, max_replace)  3
    removesuffix(obj)             1
    removeprefix(obj)             1
    rjust(max_len , obj:str)      2
    ljust(max_len, obj : str)      2
    encode()  # -> byte           0
    decode()  # str <-            0
    istitle()                     0
    isascii() # 0-126             0
    isalpha()                     0
"""

# print("Aaty".isalnum())

# print(chr(126))
# print("~".isascii())


# print("a|b|s|c".split('|'))

# a = "4 abs 4"
# print(a.strip('213'))


# join(iterable: str | list | set | dict)

# print(''.join(["a" , "b" , "c"])) # list -> str
# print(list("abc")) # str -> list
# print("a b c".split()) # str -> list

#
#
# def a(a , b):
#     pass
#
#
#
# l = [1,2,"3",4,5]
# print(''.join(l))
# print(''.join(list(map(str, l))))

# print("Name {1} , age {0}".format(24 , "Botirjon"))
# print("10".rjust(10,'|'))
# print("10".ljust(10,'|'))
# print("10".center(10,'|'))



import string
a , b = 'Hiabc', 'abc'
print((a := a.lower()).endswith((b := b.lower())) or b.endswith(a))