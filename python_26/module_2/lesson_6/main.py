sort1_list = [1, 2, 2, 2, 3, 4]
sort2_list = [1, 5, 6, 10]

ptr1 , ptr2 = len(sort1_list)-1, len(sort2_list)-1
res = []
while ptr1 >=0 and ptr2 >= 0:
    if sort1_list[ptr1] > sort2_list[ptr2]:
        res.append(sort1_list[ptr1])
        ptr1 -= 1
    else:
        res.append(sort2_list[ptr2])
        ptr2 -= 1
else:
    if ptr1 < ptr2:
        res.extend(sort1_list[:ptr2+1][::-1])

    else:
        res.extend(sort2_list[:ptr1+1][::-1])
print(res)





