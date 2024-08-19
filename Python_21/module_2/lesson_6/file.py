
"""
file access mode:
    r   -> o'qish
    w   -> yangilash
    a   -> qo'shish
    x   -> yaratish
"""
num = int(input("num : "))
s = ''
for i in range(1, num+1):
    s += f"{str(i)} "
file = open("test.txt", mode="w")
file.write(s)
file.close()
# print(file.write("123456"))
# 18:07
