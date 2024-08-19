#         item1     item2       item3        item4
# print(type(names))
# print(names[1])
# print(names[-1])
# print(names[len(names)//2])
# print(names[::2])
# print(names[::-1])

# names[1] = "Orif"
# names[2] = "Orif"
# names[1:3] = ["Orif"]
# print(names)


# l = [1,"2",3,4]
# for i in range(1,11):
#     l.append(i)
# print(l)

# ========= insert ==========
# other = ["JOhn" , "Karl"]
# other = other[::-1]
# other.append("Pub")
# print(other[::-1])

# l.insert(1 , other)
# print(l)


# ========= extend ==========
# other = ["JOhn" , "Karl"]
# other1 = ["JOhn" , "Karl"]

# other += other1
# print(other)
# other.extend(other1)
# print(other)
# ========= copy ==========
# other = ["JOhn" , "Karl"]

# l = other.copy()
# l = other[:]
# l = other[::]
# other.append(5)
# print(other)
# print(l)

# ========= remove ==========
# other = ["JOhn"]
# other.remove("Karl1")
# del other[1]
# print(other)

# ========= pop ==========
# other = ["JOhn" , 'Karl' ,1,2,2,3]
# other.pop(0) default -1
# print(other[:].clear())
# del other[2:]
# print(other)

# ============= count ==============
# other = ["JOhn",[1,2, [1,2,3]] , 'Karl' ,1,2,2,3,[1,2]]

# del other[4][2][-1]
# print(other)
# for i in range(other.count([1,2])):
#     other.remove([1,2])
# print(other)

# ============= reverse ==============
# other = ["JOhn",[1,2, [1,2,3]] , 'Karl' ,1,2,2,3,[1,2]]
# other.reverse()
# other = other[::-1]
# print(other)

# ====================================
# list("[1,2,3,4]")
# a= [1,2,3]
# print(list(str(a)))

# other = ["JOhn",[1,2] , 'Karl',[1,2]]
# print(id(other))
# other.reverse()
# index = 0
# for i in other:
#     other[index] = i[::-1]
#     index += 1
# other.reverse()
# print(id(other))
# print(other)

# =============== sort ==========


fullname = ["Alisher Ravshanov",
    "Asilbek Ziyodulayev",
    "Asliddin Qutbiddinov",
    "Azizbek Bobonazarov",
    "Bekzod Sharipov",
    "Botir Ikromjonov",
    "Davron Ubaydullayev",
    "Dostonbek Numanjanov",
    "Izzatilla Toirov",
    "Kamola Normurodova",
    "Lutfulla Abdukarimov",
    "Miraziz Erkinaliyev",
    "Muhammadyusuf Qayumov",
    "Musaxon Joraqoziyev",
    "Nurulla Ergashev",
    "Otabek Ahmadaliyev",
    "Oybek Nematullayev",
    "Sardor Akromov",
    "Sarvar Baxtiyorov",
    "Shoxruh Rahimov",
    "Sunnatillo Yoqubov",
    "Ulugbek Kuldashov"]





# def function(x):
#     return x.split()[1]
# fullname.sort(key  = function)
# print(fullname)

# b = lambda x , y : x + y
# print(b(5, "10"))


# for i in fullname:
#     # print("\n".join(i.split()))
#     print(i)
#     print()



# names = ["Kamol7", "Jamol2", "Botirjon8", "Ravshan4"]
#
# n = names.copy()
# # names.sort(key=lambda x : x[-1])
# names.sort(key=lambda x : len(x))
# # names.sort()
# print(names)

# a = [65 , 64]
# a.sort()
# print(a)

# memory management


# fullname.sort()
# s=[]
# f=[]
# index=0
# for i in fullname :
#     i=i.split()
    # s+=[i[0]]
    # f+=[i[1]]
#     s.append(i[0])
#     f.append(i[1])
#
# print(s)
# print(f)

# list comprehension

# massiv = [1,2,3,4,5,6]
# print([0 if item % 2 == 0 else item for item in massiv])
#
# b = -21
# a = 0 if b < 0 else b
# print(a)


# s = [i.split()[0][:-1] if len(i.split()[0]) % 2 == 1 else i.split()[0] for i in fullname if not i.startswith("A")]
# s = [i for i in fullname if not i.startswith("A")]
# print(s)

# l = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         l.append(i)

# print([i if i % 2 ==0 else [] for i in range(1,101)])






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

# names = []
# while True:
#     name = input("name : ")
#     names.append(name)
#     key = input("yes/No")
#     if key == "yes":
#         break
# print(names)


# algo
# 4
# 44 99 55 12
# 1 3

# l = int(input())
# massiv = list(map(int , input().split()))
# a , b = map(int , input().split())
# a -= 1
# min_num = min(massiv)
#
# while a < b:
#     massiv[a] = massiv[a]/min_num + 0.0001
#     a += 1
#
# print(massiv)
# for i in massiv:
#     print(f"{i:.1f}", end= " ")









