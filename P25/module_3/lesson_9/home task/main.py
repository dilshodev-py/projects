import json
from collections import namedtuple


with open('users.json' , 'r') as f:
    users = json.load(f)
User = namedtuple('User' , users[0].keys())

menu = """
    1) id
    2) fullname
    3) age
    >>>"""
key = int(input(menu))

for user in users:
    user_obj = User(**user)
    data = {
        1 : user_obj.id,
        2 : user_obj.fullname,
        3 : user_obj.age,
    }
    print(data[key])

