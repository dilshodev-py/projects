from collections import Counter

# l = [1,1,3,3,2,2]
# k = 3
# c= Counter(l)
# tmp = [key for key , v in c.items() if k == v]
# if (ln:=len(tmp)) < k:
#     tmp.extend(sorted(set(l))[-(k-ln):])
# else:
#     tmp = tmp[:k]
# print(tmp)

l = [1,1,1,1,2,3,5,6]
k = 4

t = l[:]

l.sort(key=lambda i: t.count(i) != k)
l = [v for i, v in enumerate(l) if v not in l[i + 1:]][:k]

print(l)



