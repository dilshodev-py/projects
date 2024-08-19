
# def count_code(str):
#   # version 1
#   # al = "abcdefghijklmnopqrstuvwxyz"
#   # count = 0
#   # for i in al:
#   #   tmp = "co" + i + "e"
#   #   if tmp in str:
#   #     count += str.count(tmp)
#   # return count
#   index = 0
#   count = 0
#   while index < len(str)-3:
#     if str[index:index+2] == "co" and str[index + 3] == 'e':
#       count += 1
#     index += 1
#   return count
#
#
#
# "codexxcode"[7 + 3]
# count_code("codexxcode")


# print("abc.xyzxyz".count('.xyz'))
# print("abc.xyzxyz".count('xyz'))



# string methods

# def swapcase(satr):
#     # version 1
#     # result = ""
#     # for i in satr:
#     #     o = ord(i) # 72
#     #     if 65 <= o <=90:
#     #         result += chr(o + 32)
#     #     elif 97 <= o <= 122:
#     #         result += chr(o - 32)
#     #     else:
#     #         result += i
#     # return result

    # # version 2
    # result = ""
    # for i in satr:
    #     if i.islower():
    #         result += i.upper()
    #     else :
    #         result += i.lower()
    # return result





# print(swapcase("Hello"))

# name = "John"
# for i in range(0 , len(name)):
#     print(name[i])


# def remove(satr , char):
#     return satr.replace(char , '')
#
#
# print(remove("Hello", 'll'))

