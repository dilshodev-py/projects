# list


# [] - list
"""
clear
copy
append
insert
extend
pop
remove
index
count
reverse
sort
"""
# () - tuple
"""
count
index
"""
# s = "apple"  # char
# mylist = ["apple", "banana", "cherry"] # item
#
#
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# list1 = ["apple", 6, "banana", 10, True, "cherry", False]
# print(*[i for i in list1 if isinstance(i , str)])
# for i in list1:
#     print(i) if isinstance(i , str) else None


# thislist = list(("apple", "banana", "cherry")) # type casting
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = 10
# print(thislist)


# thislist = ["apple", "banana", "cherry" , "orange"]
# # thislist[0] , thislist[-1] = thislist[-1] ,thislist[0]
# print([thislist[-1]]+thislist[1:-1]+ [thislist[0]])
# print(thislist)

# list1 = [1,2,3,4]
# list2 = list1[:]
# list2 = list1.copy()
# list1.append(10)
# print(list1)
# print(list2)
"""
["orange" , "banana", "cherry" , "apple"]
"""
# s = ["orange" , "banana", "cherry" , "apple"]
# s[0] , s[-1] = s[-1] , s[0]
# print(s)

# s = ["orange" , "banana", "cherry" , "apple"]
# p = s.copy()
# print(id(s))
# print(id(p))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(id(thislist))
# thislist = list(range(1,2))
# print(thislist , id(thislist))

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append(10)
# thislist.extend("a b c")
# print(thislist)

# thislist = ["apple", "banana", "cherry" , "adjvwe","banana"]
# for _ in range(thislist.count("banana")):
#     thislist.remove("banana")
# print(thislist)
# for i in thislist:
#     if i == "banana":
#         thislist.remove(i)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# h = thislist.pop(1)
# print(h)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(thislist.remove("banana"))
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# #
# print(thislist[:3])
# del thislist[1:3]
# print(thislist)
#
#
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])
#
# for i in thislist:
#     print(i)


thislist = ["a" , "b" , "c" , "d", "c"]
#
# for j in range(0 , len(thislist), 2):
#     print(thislist[j] , thislist[j+1])

for j in range(0 , len(thislist)//2 + len(thislist)%2 ):
    print(*thislist[j*2:j*2+2])



"""
a b
c d
"""




"""
apple
banana
cherry
"""
