"""
tuple
set
"""

"""     TUPLE -> ()
index
count
"""

# t = (1,2,3)
# print(id(t))
# t += (1,)
# print(id(t))
# print(t)

# list different tuple
# list - tuple

# savat 2 kg olma  3 olma   list
# import sys
# l = [1,2,3]
# print(sys.getsizeof(l))
# t = (1,2,3)
# print(sys.getsizeof(t))

# {1,2,3,4,5}   -> index yo'q , slice yo'q , takroriy element yo'q , sikl ha
# print(len({1,2,1})) # shuffle
# print({"1","2","1"}) # shuffle


s = set()
print(type(s))
s.add(1)
s.add(2)
# print(s.pop())
# print(s)
# print(s)
# s.discard(10)
# print(s)
# print(s)
# s.remove(10)
# print(s)
# s.update([1,2,3,4,5])
# print(s)

s1 = {1,10}
s2 = {1,2,3,4}
# print(s2.difference(s1))
# s2.difference_update(s1)
# print(s2)
# print(s1.intersection(s2))
# print(s1.intersection_update(s2))
# print(s1)
# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.union())
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

"""SET
add   
clear
copy
discard
difference
difference_update
intersection
intersection_update
isdisjoint
issubset
issuperset
pop
remove
symmetric_difference
symmetric_difference_update
union
update
"""







