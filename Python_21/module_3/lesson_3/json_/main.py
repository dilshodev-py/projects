# import json

# l = str(l)
# print(type(l))
# l = list(l)
# print(l)

# list()
# dict()
# str()
# int()
# float()
# bool()
# l = [1, 2, 3, 4, 5]
# l = json.dumps(l) # str
# print(type(l))
# l = json.loads(l)
# print(l)
# 15:59


# users = [
#     {
#         "id": 1,
#         "name": "Jamol"
#     },
#     {
#         "id": 2,
#         "name": "kamol"
#     }
# ]
# with open('regions.json', 'w') as f:
#     json.dump(users, f, indent=3)
#
# with open('regions.json', 'r') as f:
#     data = json.load(f)
#     print(data)

# 16:03

# with open("regions.json" , 'w') as f:
#     json_format = json.dumps(users,indent=3)
#     f.write(json_format)
#
# with open("regions.json" , 'r') as f:
#     data = json.loads(f.read())
#     print(data)


# numbers.json -> [1,2,3,4,90,6,7,8,9]

# with open("numbers.json", 'r') as f:
#     data = json.load(f)
#
# data = [i for i in data if i % 2 == 0]
#
# with open("numbers.json", 'w') as f:
#     json.dump(data, f)

# numbers.json -> [2,4,6,8]
# 16:10


# 16:20

# with open("numbers.json", "r") as f:
#     data = json.load(f)
#
# with open("regions.json", "r") as f:
#     users = json.load(f)
#
# new = [user for user in users if user.get("id") in data]
#
# with open("regions.json", "w") as f:
#      json.dump(new, f, indent=3)