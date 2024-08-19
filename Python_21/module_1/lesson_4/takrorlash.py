"""
mutable -> list , set , dict , tuple
immutable -> int , float , str , bool , complex , tuple

hashable   -> immutable
unhashable -> mutable
"""
import os
import time
"""
a= ([])
print(type(a))
"""
# a = ([])
# print(type(a))

"""
id()
oct()
hex()
int(hex() , 16)
print(obj, end = " ")
"""
# print(*[1,2,3,4,5] , sep='|')

# print(type(print()))
# print(type(None))

# a =  b , c = 1 , 2
# print(a)

"""
int function_name ( b ,a = 10) {
    return a + b
}

cout << function_name(20)
"""

# code = """
# 10+10+20-(4*5)
# """
# exec(compile(code ,filename='nimadir', mode="exec"))
# print(*range(0, 10 , 2))

# num = int(input('>>>'))
# i = 0
# while i <= num:
#     print(i)
#     time.sleep(2)
#     os.system('clear')
#     i += 1

# code = """10 + 20"""
# print(eval(compile(code, filename="nimadir", mode="eval")))

