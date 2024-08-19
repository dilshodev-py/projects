import json

"""
mode : r - o'qish 
       w - yozish
       a - qo'shish
       x - file yaratish
"""
#
# with open('users.json', mode='r') as f:
#     users = json.load(f)
#
# user = {
#     "fullname": "Botir Qodirov",
#     "age": 30,
#     "phone_number": "+998991234567",
#     "location": {
#         "long": 23456,
#         "lat": 2345
#     }
# }
# users.append(user)
# with open("users.json", mode='w') as f:
#     json.dump(users, f , indent=3)

# =================================

with open("users.json" , "r") as f:
    users = json.load(f)

for user in users:
    if user.get("fullname") == 'Botir Qodirov':
        print(user)










