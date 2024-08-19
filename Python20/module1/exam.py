# word1 = ["ab", "c"]
# word2 = ["a", "bca"]

# print("".join(word1) == ''.join(word2))

# 2

# def change_to_reverse(satr , word):
#     return satr.replace(word , word[::-1])
# print(change_to_reverse("Hello Python !!!", 'Hello'))

# 3
# nums = [11,15,7]
# target = 9

# def a(nums , target):
#     # for i in range(len(nums)):
#     #     if target - nums[i] in nums[i+1:]:
#     #         return [i, nums[i+1:].index(target-nums[i])+i+1]
#     for i in range(len(nums)):
#         for j in range(i+1 ,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
# print(a(nums, target))

# 4)
# names = ["Mary","John","Emma"]
# heights = [180,190,170]
#
# massiv = list(zip(names, heights))
# massiv.sort(reverse=True , key = lambda item : item[1])
# print([i[0] for i in massiv])

# 5)
#
# n = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# n = zip(*n)
# for i in n:
#     print(i)


# 2 variant
# 1
# s = "Hello how are you Contestant"
# k = 4
# print(" ".join(s.split()[:k]))

# 2
# allowed = "aab"
# words = ["ad","bd","aaab","baa","badab"]
# c = 0
# for i in words:
#     if set(i) == set(allowed):
#         c += 1
# print(c)


# 3
# num = 607
# num = str(num).rjust(4 , '0')
# num = sorted(list(str(num)))
# print(int(f"{num[0]}{num[-1]}")+int(f"{num[1]}{num[2]}") )

# son=9911
# son=str(son)
# r1,r2=son[:2],son[2:]
# print(int("".join(sorted(str(r1)))) +  int("".join(sorted(str(r2)))))


# 4)
# count <- sikl
# s = "cabbaaz"
# for i in range(len(s)):
#     if s[i] in s[i+1:]:
#         print(s[i])
#         break
# else:
#     print(None)


# 5

# nums = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
# summ = sum(nums[0] + nums[-1])
# for i in nums[1:-1]:
#     summ += i[0] + i[-1]
# print(summ)


# s= "Hello how are you Contestant"
# k = 4
# a=""
# for i in s.split():
#     if i == k:
#         a+=i
#     else:
#         print(i)
#         break
# print(a)

# allowed = input('allowed: ')
# s = input('listni kiriting: ')
# words = [int(i) if i.isdigit() else i[1:-1:] for i in s[1:-1:].split(',')]
# while True:
#     words.append(input('Item: '))
#     n = input('Do you want continue Y/n: ')
#     if n == 'n':
#         break
# n = 0
# for i in words:
#     if allowed in i:
#         n += 1
# print(n)


# s = input()
# nums = [i.split(',') for i in s[2:-2:].split('],[')]
# print(nums)
# y = 0
# for i in range(len(nums)):
#     for j in range(len(nums[0])):
#         if i == 0 or j == 0 or j == len(nums[0]) - 1 or i == len(nums) - 1:
#             y += int(nums[i][j])
# print(y)



