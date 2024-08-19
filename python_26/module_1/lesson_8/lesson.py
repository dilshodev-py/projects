

# l1 = [1,2,2,3]
# l2 = ["a" , "b" , "c"]
# print(l1.count(2))
# l2.extend("abs") # str , list , tuple , set
# print(l2)

# ========= sort ==============

# l = ["Abdurashid" , "Kamola" , "Rasul" , "Botir"]
# l.sort(key= lambda x : x[-1] , reverse=True)
# print(l)

# [10,5,4]
# l = [(10,20),(1,2) , (4,3) , (7,9) ]
# l.sort(key= sum)
# print(l)



# l = ["Abdurashid",1 , "Kamola" ,10, "Rasul" , "Botir"]
# l.sort(key = lambda x : x if isinstance(x , int) else ord(x[0]))
# print(l)
# l.sort(key = lambda x : x.count('a') + x.count("A"))
# l.sort(key = lambda x : x.lower().count('a')) ,print(l)
# print(sorted(l, key=lambda x: x.lower().count('a')))


# nums = [0,2,1,5,3,4]
# result = []
# for i in nums:
#     result.append(nums[i])
# print(result)

# print([nums[i] for i in nums])


# nums = [1,2,3,1,1,3]

# ======= 1-usul ===============
# tmp = []
# good_pair = 0
# for i in nums:
#     if not i in tmp:
#         tmp.append(i)
#         n = nums.count(i)
#         good_pair += n*(n-1)//2
# print(good_pair)

# =========== 2-usul ============

# print(sum([(n:=nums.count(i))*(n-1)//2 for i in set(nums)]))

# from itertools import combinations
# nums = [5,1,6]
# summ = 0
# for i in range(1,len(nums)+1):
#     combinations_ = list(combinations(nums, i))
#     for combinat in combinations_:
#         tmp = 0
#         for j in combinat:
#             tmp ^= j
#         summ += tmp
# print(summ)


# 2 + 3 = (5 >= max)  True
# 3 + 3 = (6 >= max)  True
# 5 + 3 = (8 >= max)  True
# 1 + 3 = (4 >= max)  False
# 3 + 3 = (6 >= max)  True
# [True , True , True , False ,True]
# candies = [2,3,5,1,3]
# extraCandies = 3
# print([i + extraCandies >= max(candies) for i in candies])

# maxi = max(candies)
# for i in candies:
#     result.append(i + extraCandies >= maxi)
# print(result)


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

# lowercase = "abcdefghijklmnopqrstuvwxyz"
# key = key.replace(" ", "")
# tmp = ""
# for i in key:
#     tmp += i if not i in tmp else ""
# key = tmp
# return "".join([" " if i == " " else lowercase[key.index(i)] for i in message])

"""
abcdefghijklmnopqrstuvwxyz
thequickbrownfxjmpsvlazydg
"""


# words = ["abc","car","ad","racecr","cool"]
#
# print(([i for i in words if i == i[::-1]]+[""])[0])

# for i in words:
#     if i == i[::-1]:
#         print(i)
#         break
# else:
#     print("")















