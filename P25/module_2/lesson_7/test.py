""""""
"""
mode:
    r x a w
    
path:
    absolute path - /home/dilshod/PycharmProjects/P25/module_2/lesson_7/task.txt
    relative path - module_2/lesson_7/task.txt
"""


# file = open('numbers.txt' , mode='r')
#
# for i in file:
#     print(i)
# file.close()

# print(file.readline())
# file.seek(0)
# print(file.readline())
# file.seek(0)
# print(file.readline())
# file.close()
# print(file.readlines(8))
# =================================


# num = int(input("Num : "))
# s = ""
# for i in range(num + 1):
#     if i % 2 == 0:
#         s += str(i) + " "
#
# file = open('nums.txt' , mode='w')
# file.write(s)
# file.close()


# ====================================



# file = open('nums.txt' , mode = 'r')
# numbers = file.read().split()
# result = ""
# for i in numbers:
#     if int(i) % 2 != 0:
#         result += i + " "
# file.close()
#
# file = open("nums.txt" , mode='w')
# file.write(result)
# file.close()



# ========== task 3===================================


# f = open("sample.txt" , 'r')
# for i in f.readlines():
#     print(i)

# ========== task 4===================================

# f = open("sample.txt" , 'r')
# for i in f.readlines():
#     if 'satr' in i:
#         print(i)

# ========== task 5===================================

# f = open("sample.txt", 'r')
# data = f.read().lower()
# f.close()

# file = open('sample.txt' , 'w')
# file.write(data)
# file.close()


# =========== task 6==============================
# text = """ism,yosh
# Ali,25
# Vali,30
# Sarvar,22"""
#
# file = open('data.txt' , mode='w')
# file.write(text)
# file.close()

# =========== task 7==============================

#
# f = open("data.txt" , 'r')
# text = f.readlines()
# f.close()
#
# result = ""
# for i in text[1:]:
#     if int(i.split(',')[1]) >= 25:
#         result += i
# print(result)
# f = open('filtered_data.txt' , 'w')
# f.write(result)
# f.close()

# ============

# with open("books.txt" , 'r') as f:
#     data= f.readlines()
#
# result = ""
# for i in data:
#     if int(i.split(',')[1]) >= 80:
#         result += i
#
# with open("top_students.txt" , 'w') as f:
#     f.write(result)


# =======================================


# with open("books.txt" , 'r') as f:
#     data= f.readlines()

# result = []
# for i in data:
#     result.append(int(i.split(',')[1]))
#
# print(sum(result)/len(result))



