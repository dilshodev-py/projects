"""
print
input
variable
value
hash       -> immutable
unhashable -> mutable
immutable  -> str ,bool , int  , float , complex , tuple
mutable    -> list , set , dict , tuple
id
chr
ord
compile -> str(code) -> python
exec    -> str(code) -> python -> run
eval    ->
len
type
#
memory -> stack(var) , heap(value)
hex -> 16
bin -> 2
oct -> 8
int -> 10
def function_name(*arg1):
    logic
    return 
    print(10)

l = (1,2,3,4,5,6,7,8,9)
function_name(1,2,3,4,5,6,7,8,9)

    
unpacking
    a , b , c = [1,2,3]
    
packing

    a = 1,2,3
    def function_name(*arg , kwargs)
    function_name(1,2,3,4,5,6,7,8,9 , a = 1)
    
    


string
    "" , '' , """""" , '''''' , str(10)
    \t , \n  
    1 tab - 4 probel
    X str -> hammasi
    str -> other type -> 
    
    methods
        split()
        
        

            

"""

# print("10 - 20 * ( 1 / 2)")
# print(int(eval("10 - 20 * ( 1 / 2)")))

# def function(a, b ,/, y ,*, c , d):
#     pass
#
# function(a = 1 , b = 10 , c = 20  , d = 8)


# print(int(float("10.1")))
# print(.19)
# print(bool(" "))
# print(list("[1,2,3,4]"))
# print(list("hello"))
# print(list(str([1,2,3,4])))


# for i in list(range(row//2))[::-1]:
#     print((c*(2*i+1)).center(col , "-"))


# print(range(1 , 100)[::-1])
# row, col = map(int, input().split())
#
# c = ".|."
# for i in range(row // 2):
#     print(i)
#     print((c * (2 * i + 1)).center(col, "-"))
# print("WELCOME".center(col, '-'))
# for i in range(row//2-1, 0, -1):
#     print((c * (2 * i + 1)).center(col, "-"))

# for i in range(10 , 0 , -2):
#     print(i)
# print(1 in range(2,10))

# size 5
import string

# alpha = "abcdefghijklmnopqrstuvwxyz"
# # --------e--------
# # ------e-d-e------
# # ----e-d-c-d-e----
# # --e-d-c-b-c-d-e--
# # e-d-c-b-a-b-c-d-e
# # --e-d-c-b-c-d-e--
# # ----e-d-c-d-e----
# # ------e-d-e------
# # --------e--------
#
# size = int(input(">>>"))
# al1 = alpha[:size]
# al2 = al1[::-1]
#
# for i in range(1, size+1):
#     print(('-'.join(list(al2[:i])) + "-" +'-'.join(list(al1[:i]))).center(4*size-3 , '-'))
#
#
# for i in range(size-1,0, -1):
#     print(('-'.join(list(al2[:i])) + "-" +'-'.join(list(al1[:i]))).center(4*size-3 , '-'))


# size 5


sentences = ["alice and bob love leetcode",
             "i think so too",
             "this is great thanks very much"]

# def mostWordsFound(sentences : list[str]) -> int:
# 1 version
# maxi = len(sentences[0].split())
# for sentence in sentences:
#     if maxi < len(sentence.split()):
#         maxi = len(sentence.split())
# return maxi

# 2 version
#     return len(sorted(sentences, key=lambda x: len(x.split()))[-1].split())
#
# print(mostWordsFound(sentences))

# i = input(">>>") # ikki
#
# print(i == i[::-1])


# word = "Lor56em2"

# son = ""
# summ = 0
# for i in word:
#     if i.isdigit():
#         son += i
#     elif son:
#         summ += int(son)
#         son = ""
# summ += int(son)
# print(summ)

# a = "Lorem Ipsum        is       simply "
# Lorem Ipsum is simply
# 1 version
# print(" ".join(a.split()))
# print(*a.split())


# a = "Lorem Ipsum is simply"
# 1 version
# result = ""
# for i in a.split():
#     result += i[::-1] + " "
# print(result)

# 2 version
# print(*a[::-1].split()[::-1])


# a = "Lorem Ipsum yui is simply"
#
#
# print((i:=a.split())[(o:=len(i)//2)][len(i[o])//2])

# print("8" in "hgasvdgavef7")

"""
"hPrBKWDH8y8c6Lt5NQZWQ"  -->  "865"


"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"


"555"                   -->  "5"
"""

# a = "hPrBKWDHycLtNQZWQ"
# print(a)
# res = "8"
# for i in a:
#     if i.isdigit() and i not in res:
#         res += i
#
# print(res) if res else print("One more run !")






def shifr(matn):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in matn:
        if i == "z":
            res += "z"
        else:
            res += alpha[alpha.index(i) + 1]
    return res


def deshifr(shifr_matn):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # bjpq
    res = ""
    for i in shifr_matn:
        if i == "z":
            res += "z"
        else:
            res += alpha[alpha.index(i) - 1]
    return res


print(shifr("aiop"))
print(deshifr("bjpq"))



