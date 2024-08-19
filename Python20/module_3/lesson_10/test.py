l = [1,2,3,4,5]
k = 2

for i in range(0 , len(l) , k):
    if len(l[i : i+k]) == k:
        l[i : i+k] = l[i : i+k][::-1]
print(l)



