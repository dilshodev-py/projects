

""""""

# with open("file_path" , mode="[r , w , a , x]") as f:
    # f.read()
    # f.write("str_data")
    # f.seek(1)
    # f.readline()
    # f.readlines()
    # pass


# with open('books.txt' , 'r') as f:
#     data = f.readlines()
#
# result = []
# for i in data:
#     book_name , author = i.split(',')
#     fullname_reverse = " ".join(author.split()[::-1])
#     result.append(f"{book_name}, {fullname_reverse}\n")
#
# with open('books.txt' , 'w') as f:
#     f.writelines(result)

# with open('employess.txt' , 'r') as f:
#     data = f.readlines()
#
# result = []
# for i in data:
#     fullname , role , salary = i.split(',')
#     if fullname.strip() == 'Sarah Johnson':
#         salary = " 4000"
#
#     result.append(f"{fullname},{role},{salary}")
#
# with open('employess.txt' , 'w') as f:
#     f.writelines(result)


# with open('movies.txt' , 'r') as f:
#     data: list[str] = f.readlines()
#
# data = sorted(data , key=lambda x : float(x.split(',')[-1]))
# print(*data[-3:])

# min_ = float(input("Min reyting : "))
# max_ = float(input("Max reyting : "))
# with open('movies.txt' , 'r') as f:
#     data: list[str] = f.readlines()
#
# for i in data:
#     reyting = float(i.split(',')[-1] )
#     if min_ <= reyting <= max_:
#         print(i, end='')


# with open("movies.txt" , 'r') as f:
#     data: list[str] = f.read().split()
#
# d = {}
# d = d.fromkeys(data , 0)

# for i in data:
#     d[i] += 1
# del d[',']
# print(max(d.items(), key=lambda x: x[1])[0])










