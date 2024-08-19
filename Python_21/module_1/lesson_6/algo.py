"""https://algo.ubtuit.uz/problem/150"""

# s = input().split()
# for i in s:
#     if 'info' in i.lower():
#         print(i, end=' ')

"""https://algo.ubtuit.uz/problem/149"""

# s = input().split()
# c = 0
# find_str = ''
# for i in s:
#     if i.endswith('NA'):
#         c += 1
#         find_str += i + " "
# print(f"{c}\n{find_str}")

"""https://algo.ubtuit.uz/problem/153"""

# s = input().split() # [ALGORITM ,TUIT, UZ]
# for i in s:
#     print(i, len(i))

"""https://algo.ubtuit.uz/problem/154"""

# num = input() # "123"
# s = 0
# for i in num:
#     if i.isdigit():
#         s += int(i)
# print(s)

"""https://algo.ubtuit.uz/problem/156"""

# s = input().split()
# i , j = map(int , input().split())
# s[i-1] , s[j-1] =  s[j-1] , s[i-1]
# print(' '.join(s))

# val1 = s[i-1]
# val2 = s[j-1]
# for place in range(1,len(s)+1):
#     if place == i:
#         s[i-1] = val2
#     if place == j:
#         s[j-1] = val1

"""https://algo.ubtuit.uz/problem/157"""

# s = input().split()
# place = int(input())
# s[place - 1] = "TATU"
# print(" ".join(s))

"""https://algo.ubtuit.uz/problem/161"""

# max_card = int(input())
# cards = input()
# tmp = "ASSALOM"


# for i in tmp:
#     c1 = tmp.count(i)
#     c2 = cards.count(i)
#     if c1 > c2:
#         print("NO")
#         break
# else:
#     print("YES")

"""https://algo.ubtuit.uz/problem/162"""

# n = int(input()) , print(input().replace("$", ""))


"""https://algo.ubtuit.uz/problem/164"""

# matn = input()
# L , R = map(int , input().split())

# print(matn[R-1 : L][::-1]) if R < L else print(matn[L-1 : R])



# def replace_substring(obj:str , old:str , new:str) -> str:
#     return obj.replace(old , new)
#
#
# print(replace_substring("12345677", "7", "8"))


# def remove_duplicates(input_str : str) -> str:
#     result = ''
#     for i in input_str:
#         if not i in result:
#             result += i
#     return result
#
# print(remove_duplicates("aabcccr"))



# def format_phone_number(phone_number):
#     code = ["99" , "97" , "93" , "88" , "98" , "91" ,"90" ,"55" , "70" , "71" , "94" , "50" , "33"]
#     phone_number = phone_number.replace(" ", "")
#     phone_number = ("" if phone_number.startswith("+998") else "+998") + phone_number
#     if len(phone_number) != 13:
#         return "Phone number invalid"
#     if not phone_number[4:6] in  code:
#         return "code not found !"
#     return  "🟢" + phone_number
#
#
# print(format_phone_number("88 333 22 1"))
#


# def com_string(matn):
#     result = ''
#     c = 1
#     end = matn[0]
#     for i in matn[1:]:
#         if i == end:
#             c += 1
#         else:
#             result += f"{end}{c}"
#             c = 1
#             end = i
#     else:
#         result += f"{end}{c}"
#     return result
#
#
# print(com_string("abbbbc"))


# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi Hi"

# def remove(matn: str) -> str:
#     matn = matn.split()
#     result = ""
#     for i in matn:
#         result += i.rstrip("!") + " "
#     return result.strip()
#
#
# print(remove("hi!"))
#
#
# print("hi" == "hi")
#


"""
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi!!"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
"""

# print("hi".removesuffix("!"))


"""

esrever("Much l33t?") == "t33l hcuM?"

esrever("tacocat!") == "tacocat!"
"""

def esrever(matn):
    l = matn[:-1][::-1] + (matn[-1] if matn else '')
    return l
#
# esrever("") #  "dlrow olleh."


# print(""[-1])

# print(isinstance(esrever(""), str))

# operations = ["X++","++X","--X","X--"]
# count=0
# for i in operations :
#     count += -1 if "-" in i else 1
# print(count)


jewels = "aA"
stones = "aAAbbbb"
c = 0
for i in jewels:
    c += stones.count(i)
print(c)

