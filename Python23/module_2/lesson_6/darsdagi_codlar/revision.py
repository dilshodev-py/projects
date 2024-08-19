# ============= rivision ==============

# open(file_path , mode = '[r , w , x , a]')


# file = open("/home/dilshod/PycharmProjects/Python23/module_2/lesson_6/task.txt" , 'r')
# print(file.read())
# print(file.readline(10))
# print(file.readline(10))
# print(file.readline(10))
# print(file.readlines(5))
# file.seek(2)
# print(file.read())
# file.close()
# from string import ascii_uppercase
#
# result = ""
# for i , v in enumerate(ascii_uppercase):
#     result += f"{i} {v}\n"
#
# with open("task1.txt" , 'w') as file:
#     file.write(result)
#
# file = open("task1.txt" , "w")
# file.write(result)
# file.close()

# l = ["bir" , "ikki" , "uch"]
# for i , v in enumerate(l):
#     print(i , v)

# n = int(input(">>")) # 5
# shape = ""
# for i in range(n-1):
#     shape += "*\n"
# shape += "* "*n
#
# with open("task2.txt", 'w') as file:
#     file.write(shape)

# n = int(input("n: "))
# tshape = ""
# tshape += "* " * n + "\n"
# for i in range(n-1):
#     tshape += "  "* (n//2) + "*\n" if n % 2 == 1 else " "* (n-1) + "*\n"
# print(tshape)

# with open("tshape.txt", "w") as file:
#     file.write(tshape)
# num>>> 3
# * * *
#   *
#   *
# num>>> 4
# * * * *
#    *
#    *
#    *

# 15:49

class A:

    @classmethod
    def a(cls):
        print(cls.__name__)
        return cls(1)

class B(A):
    def __init__(self , b  = None):
        self.b = b


print(B().a().b)



