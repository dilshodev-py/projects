""""""
"""
          task 1
          
a o'zgaruvchidagi raqamlar yig'indilari topilsin

input: a = "Lo1rem 2is l3ong4"
output: 10
14:45

                task 2
input : a = "Lo1rem 2is l3ong4"
output: Lorem is long
14:54

                task 3
                
{ count == ( count  and  } count == ) count      
input : a = "{}()}"
output: False
15:03

                task 4
                
input : a = "Lo1rem 2is l3ong4"
output: Lorem is long 1234
15:12

                task 5  
                
add('a', 'b' , "hh" , "asdfgf") -> ascii id sum(97 + 98 + 208 = 403)
15:24

                task 6
                
def sum_str(a, b):
    pass
    
sum_str("", "") -> None
sum_str("4", "") -> 4
sum_str("4", "5") -> 9
15:37


                task 7

{} soni == () soni 
input : a = "(){}()(){}{}{}"
output: False
15:55

                    task 8
Agar so'zda 3 dan ortiq harf bo'lsa:
 1. So'zning birinchi harfini oling va uni oxirigacha ko'chiring 
 2. So‘zga -il qo‘shiladi Aks holda, so'zni yolg'iz qoldiring.
 input :  a = 'hello' 
output : 'ellohil'

input : a = "hi"
outpur : "hi"
16:00

                task 9
                
input : a = "1234567890dpqoOaAbBQ"
outpu : 16
16:10


                task 10
                
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
16:41

                task 11
                
operations = ["--X","X++","X++" , "X--"]
-1 + 1 + 1 + (-1) = 0
time : 16:46

                task 12
                
input : jewels = "aAb" , stones = "aAAbbbb"
output : 7
15:57

                task 13
Input: command = "G()()()()(al)"
Output: "Gooooal"
G -> G
() -> o
(al) -> al
17:07
[start:end:step]
                task 14
input : sentences = ["alice and bob love leetcode", 
                     "i think so too", 
                     "this is great thanks very much"]
output : 6
17:20

                task 15
Input: word1 = ["a", "b", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

"""
# word1 = ["a", "b", "cy"]
# word2 = ["a", "bc"]
# word1 = "".join(word1)
# word2 = "".join(word2)
# print(word1 == word2)


# input : sentences = ["alice and bob love leetcode",
#                      "i think so too",
#                      "this is great thanks very much"]
# output : 6


# sentences = ["alice and bob love leetcode",
#              "i think so too",
#              "this is great thanks very much"]
# maxi = 0
# for i in sentences:
#     print(i.split())
#     if maxi < len(i.split()):
#         maxi = len(i.split())
# print(maxi)


# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# command = "G()()()()(al)"
# print(command.replace("()" , "o").replace("(al)" , "al"))


# input : jewels = "aAb" , stones = "aAAbbbb"
# output : 7
# jewels = "aAb"
# stones = "aAAbbbb"
# summ = 0
# for i in jewels:
#     summ += stones.count(i)
# print(summ)


# operations = ["--X","X++","X++" , "X--"]
# -1 + 1 + 1 + (-1) = 0
# summ = 0
# for i in operations:
#     if '-' in i:
#         summ -= 1
#     else:
#         summ += 1
# print(summ)


# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# address = "1.1.1.1"
# print(address.replace("." , "[.]"))


# input : a = "1234567890dpqoOaAbBQ"
# outpu : 16
# a = "1234567890dpqoOaAbBQ"
# two_ = "B8"
# one_ = "qopRPQOabAdDg690e"
# summ = 0
# for i in a:
#     if i in one_:
#         summ += 1
#     elif i in two_:
#         summ += 2
# print(summ)

# input: a = "Lo1rem 2is l3ong4"
# output: 10
# a = "Lo1rem 2is l3ong4"
# summ = 0
# for i in a:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# input : a = "Lo1rem 2is l3ong4"
# output: Lorem is long
# a = "Lo1rem 2is l3ong4"
# result = ''
# for i in a:
#     if not i.isdigit():
#         result += i
# print(result)

# input : a = "{}()}"
# output: False
# a = "{}()}"
# if a.count("{") == a.count("(") and a.count("}") == a.count(")"):
#     print(True)
# else:
#     print(False)
#
# print(ord("h"))

# input : a = "Lo1rem 2is l3ong4"
# output: Lorem is long 1234
# a = "Lo1rem 2is l3ong4"
# string = ""
# numbers = ""
# for i in a:
#     if i.isdigit() :
#         numbers += i
#     elif i.isalpha() or i.isspace():
#         string += i
# print(string , numbers)

# add('a', 'b' , "hh" , "asdfgf") -> ascii id sum(97 + 98 + 208 = 403)

# def add(*args):
#     join_str = "".join(args)
#     summ = 0
#     for i in join_str:
#         summ += ord(i)
#     return summ

# massiv: list = input().split()
# print(add(*massiv))
# print(add("a" , "b" , "hh"))


# def sum_str(a, b):
#     if a == "" and b == "":
#         return None
#     if a == "" or b == "":
#         if len(a) > 0:
#             return a
#         else:
#             return b
#     return int(a) + int(b)


# print(sum_str("", ""))
# print(sum_str("4", ""))
# print(sum_str("4", "90"))


# sum_str("", "") -> None
# sum_str("4", "") -> 4
# sum_str("4", "5") -> 9


# {} soni == () soni
# input : a = "(){}()(){}{}{}"
# output: False
# a = "(){}()(){}{}{}"
# print(a.count("()") == a.count("{}"))


#  input :  a = 'hello'
# output : 'ellohil'
# a = 'hello'
# if len(a) > 3:
#     print(a[1:] + a[0] + "il")
# else:
#     print(a)
