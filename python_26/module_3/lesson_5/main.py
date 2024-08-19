# import csv
#
# with open('emloyee_file.csv', 'w') as csvfile:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter='|')
#
#     writer.writeheader()
#     writer.writerows([
#         {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#         {'emp_name': 'Eric Meyers', 'dept': 'IT', 'birth_month': 'March'},
#         {'emp_name': 'Eric Meyers', 'dept': 'IT', 'birth_month': 'March'},
#         {'emp_name': 'Eric Meyers', 'dept': 'IT', 'birth_month': 'March'},
#         {'emp_name': 'Eric Meyers', 'dept': 'IT', 'birth_month': 'March'},
#         {'emp_name': 'Eric Meyers', 'dept': 'IT', 'birth_month': 'March'},
#         {'emp_name': 'Eric Meyers', 'dept': 'IT', 'birth_month': 'March'},
#     ])


# import pandas as pd
# # d = {"name" : "Botir" , "age" : 25}
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# d= pd.DataFrame(data)
#
# print(d)

# import pandas as pd
#
# df = pd.read_csv('/home/dilshod/PycharmProjects/python_26/module_3/lesson_5/tasks/centers.csv',)
# df.to_excel('centers.xlsx',index=False)
# df.to_json('centers.json',index=False, orient='records', indent=3)
# print(df.to_dict(orient='records'))

#
# import numpy as np
#
# arr = np.array(1 , ndmin=5)
#
# print(arr)

# import numpy as np
#
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# print(arr.shape)

# data = pd.Series(d,index=['age'])
# print(data)

# import numpy as np
#
# arr = np.array([1, 2, 3, 4], ndmin=5)
#
# print(arr)
# print('shape of array :', arr.shape)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# print(arr.reshape(2, 4))


# import numpy as np
#
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# for x in arr.reshape(-1):
#   print(x)



from collections import UserString, namedtuple, Counter

import requests

#
#
# s = UserString('Hello World !')

# User = namedtuple('User' , ['id' , 'name' , 'address'])


# class User:
#     def __init__(self, id, name, address):
#         self.id = id
#         self.name = name
#         self.address = address

# user = User(1 , 'Botir' , 'Tashkent')


# a = "Hello World"
# print(Counter(a))
# print(len(a))

# collections
# itertools
# pandas
# numpy




"""
Lorem Ipsum is simply +998993583234 dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an +998993583234 unknown printer took a galley of type and scrambled it to make a 
 type specimen book. It has survived not only five centuries, +998993583234 but also the
  leap into electronic typesetting, +998993583234remaining essentially unchanged. It was 
  popularised in the 1960s with the release of Letraset sheets +998993583234 containing Lorem 
  Ipsum passages, and more recently with desktop publishing software like Aldus 
  PageMaker including versions of Lorem Ipsum
"""


# l = range(1, 1000)


# l -> matrix  : shape : 2 , 300


# send requests -> telegra.ph(photo)
#
# response <- https://telegra.ph/file/f7aadb6d595a7d210b206.png

# requests.post()


