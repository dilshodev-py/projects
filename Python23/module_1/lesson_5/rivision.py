"""RIVISION"""
"""
id()       address
print()    chop etish
input()    kiritish
len([str , list , tuple , dict , set])      uzunlik
type()     turini aniqlash
list()     data type
map()      array
PEP8       python rules
slice      [start:end:step]
bin()      2 lik
oct()      8 lik
hex()      16 lik
pow()      daraja
type casting   :  other type -> type
type hinting   :  a : str = 10
split()           str -> massiv
memory()       -> stack[var]    heap[value]
sqrt()         ildiz
max()          max
min()          min
from math import * -> log() , log10() , log2() , log(val , base) , sqrt()
if , if, elif , else 
for           massiv uzunligiga qarab
while         condition
lambda args : logic        nomsiz function
def function_name(arg1 , arg2 ....) -> int:
    logic
    
or   
and
not
is      check address
==      check value
4/2     2.0     
4//2    2
4%2     0
a+=1    a = a + 1        
-=
*=
**=
range(0 , 20, 2) 
packing     a = 1 , 8
unpacking   a , b = 1 , 8
eval()      "9 + 8 * (7 - 7)"
immutable    -> intervyu 
mutable      -> intervyu

"""

# function -> def , lambda

# def function_name(arg1 , arg2) -> type:
#     result = 0# logic
#     return result
# **kwargs , *args , * , / , string

"""aioue"""
def vowel_count(sentence : str) -> int:
    """nimadir"""
    c = 0
    for i in sentence:
        if i in "aioueAIOUE":
            c += 1
    return c
# leetcode
# codewars
result = vowel_count("I have got a car")
print(result)





