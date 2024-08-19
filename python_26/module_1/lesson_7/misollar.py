# ================== algo =================


# 156:

# text = input().split()
# i , j = map(int, input().split())
#
# text[i-1] , text[j-1] = text[j-1], text[i-1]
# print(" ".join(text))

# 161:

# tmp = "ASSALOM"
# int(input())
# karta = input().split()
# for i in tmp:
#     if tmp.count(i) > karta.count(i):
#         print("NO")
#         break
# else:
#     print("YES")


# leetcode : https://leetcode.com/problems/find-words-containing-character/description/
# words = ["abc","bcd","aaaa","cbc"]
# x , result= "a" , []
# for index , word in enumerate(words):
#     if x in word:
#         result.append(index)
# print(result)

# s = "RLRRLLRLL"
# balance = 0
# count = 0
# for i in s:
#     balance += 1 if i == "R" else -1
#     if not balance:
#         count += 1
#
# print(count - bool(balance))


# leetcode : https://leetcode.com/problems/truncate-sentence/description/
# s = "What is the solution to this problem"
# k = 4
# print(" ".join(s.split()[:k]))

# print(print("Hello"))


# text = "dsffdg          errtrhytj                    regthy                         th5y      rgt"
# print(' '.join(text.split()))
# print(*text.split())

# print(bool(""))
# if [0]:
#     print("hi")
# else:
#     print("bye")

# input(input())
