"""
# 0. hashable , unhashable
# 1. immutable , mutable




# 1. list function
# 2. methods
# 3. indexing
# 4. slicing
# 5. loop on list
"""

"""
hashable -> str  ,int , float , tuple , complex
unhashable - > list , set , dict_ , tuple

immutable -> hashable
mutable -> unhashable

"""
a = (1,2,3)
print(id(a))
a = list(a)
print(id(a))

a1 = [1,2,3]
a2 = [1,2,3]
a1.append(a2)
print(a1)
print(a2)
"""
append   ✅
insert   ✅
extend   ✅
copy     ✅
remove   ✅
pop      ✅
clear    ✅
index    ✅
count    ✅
reverse  ✅
sort     ✅
"""



