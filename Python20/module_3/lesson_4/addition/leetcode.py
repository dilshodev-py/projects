# pattern = "abba"
# s = "dog cat cat fish"
# s=  s.split()
# if len(s) != len(pattern):
#     return False
# d = {}
# for i in range(len(s)):
#     if pattern[i] in d:
#         if d.get(pattern[i]) != s[i]:
#             return False
#     else:
#         d[pattern[i]] = s[i]
# if len(set(d.values())) == len(d.values()):
#     return True
# else:
#     return False

# nums = [1,2,3]
# [[] ,[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
#
# def subset(nums):
#     result = [[]]
#     for num in nums:
#         tmp = []
#         for curr in result:
#             tmp += [curr + [num]]
#         result += tmp
#         # result += [curr + [num] for curr in result]
#     return result
#
# nums = [1,2,3]
# print(subset(nums))

