# (olympic_ring('wHjMudLwtoPGocnJ'), 'Bronze!')
# (olympic_ring('eCEHWEPwwnvzMicyaRjk'), 'Bronze!')
# (olympic_ring('JKniLfLW'), 'Not even a medal!')
# (olympic_ring('EWlZlDFsEIBufsalqof'), 'Silver!')
# (olympic_ring('IMBAWejlGRTDWetPS'), 'Gold!')

"""
agar ball 1 yoki undan kam bo'lsa, "Not even a medal!" deb qaytaring;
agar ball 2 bo'lsa, "Bronze!"ni qaytaring; 
agar ball 3 bo'lsa, "Silver!" 
agar ball 3 dan ortiq bo'lsa, "Gold!"ni qaytaring;
"""
"abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# alpha = 'abdegopqDAOPRQ'
# string = "IMBAWejlGRTDWetPS"
# summ = 0
# for i in string:
#     if i in alpha:
#         summ+=1
#     elif i=='B':
#         summ+=2
# res=summ//2
# if res<=1:
#     print("Not even a medal!")
# elif res==2:
#     print("Bronze!")
# elif res==3:
#     print("Silver!")
# elif res>3:
#     print("Gold!")


# =============================
# print(sorted([111, 112, 113, 114, 115, 113, 114, 110])[::-1])
#
# # o    p    q    r    s    q    r    n
# a = [111, 112, 113, 114, 115, 113, 114, 110] # , "oprn-nors-sron-nors" # original
#
# # n    o    p    q    q    r    r    s
# [110, 111, 112, 113, 113, 114, 114, 115], "oprn-nors-sron-nors" # o'sish
#
#
# sorted([111, 112, 113, 114, 115, 113, 114, 110])[::-1]   # reverse

#
# print(chr(111) , end = " ")
# print(chr(112) , end = " ")
# print(chr(113) , end = " ")
# print(chr(114) , end = " ")
# print(chr(115) , end = " ")
# print(chr(113) , end = " ")
# print(chr(114) , end = " ")
# print(chr(110) , end = " ")


# arr = [111, 112, 113, 114, 115, 113, 114, 110]
# var1 = f"{chr(arr[0])}{chr(arr[1])}{chr(arr[-2])}{chr(arr[-1])}"
# arr = sorted(arr)
# var2 = f"{chr(arr[0])}{chr(arr[1])}{chr(arr[-2])}{chr(arr[-1])}"
#
# print(f"{var1}-{var2}-{var2[::-1]}-{var2}")
# alpha = "zyxwvutsrqponmlkjihgfedcba!? "
# # ['24', '12', '23', '22', '4', '26', '9', '8'], 'codewars'
#
# arr = ['24', '12', '23', '22', '4', '26', '9', '8']
# result =""
# for i in arr:
#     result+=alpha[int(i)-1]
# print(result)

# "+-*/"
# l = [89 , 900 , 123 , 369 , 246 ,90 , 78]
#
# operator = ["+" , "-" ,"*" , "/"]
#
# result = l[0]
# index = 0
# for i in l[1:]:
#     result = eval(f"{result} {operator[index]} {i}")
#     index += 1
# print(result)


# string = "((((89 + 900)- 123) * 369) / 246)"
# print(eval(string))

"""
list methods
list
misolga yondashish
5 soat dars o'tish

"""






