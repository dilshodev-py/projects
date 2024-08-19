# from string import ascii_letters as al
#
# start_alpha , end_alpha = input().split('-')
# print(al[al.find(start_alpha):al.find(end_alpha) + 1])
#

# https://www.codewars.com/kata/64fc03a318692c1333ebc04c

# def best_friend(txt, a, b):
#     # lis=[]
#     # for i in range(len(txt)-2):
#     #     if txt[i]==a and txt[i+1]==b:
#     #         lis.append(True)
#     #     elif txt[i]==a and txt[i+1]!=b:
#     #         lis.append(False)
#     # if txt[-1]==a or False in lis:
#     #     return False
#     # return True
#     for i in range(len(txt) - 1):
#
#         if txt[i]==a and txt[i+1]!=b:
#             return False
#
#     if txt[-1]==a:
#         return False
#     return True
#
#
# a=best_friend("ifcygbbyg nhygayg aygv aaygjygcygyv", 'y', 'g')
# print(a)

# def sort_grades(lst):
#     for i1 , v1 in enumerate(lst):
#         for i2 , v2 in enumerate(v1):
#             if isinstance(v2 , list):
#                 lst[i1][i2] = v2.sort(key= lambda x : x[1:])
#     return lst

# def scramble(strng, array):
#     arr=array.copy()
#     for i in range(len(strng)):
#         arr[array[i]]=strng[i]
#     return "".join(arr)
# scramble('abcd', [0, 3, 1, 2])


# def build_string(*args):
#     return "I like"+",".join(args)+"!"








