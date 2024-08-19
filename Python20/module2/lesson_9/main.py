# import json
# class File:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def read(self):
#         with open(self.file_path , 'r') as f:
#             data: list[dict] = json.load(f)
#         return data
#
#     def write(self , data : list[dict]):
#         with open(self.file_path , 'w') as f:
#             json.dump(data , f , indent=3)
#
#
# posts : list[dict] = File("posts.json").read()
# albums : list[dict] = File("albums.json").read()
# users : list[dict] = File("users.json").read()
#
# for ui, user in enumerate(users):
#     for album in albums:
#         if user.get('id') == album.get("userId"):
#             users[ui]['albums'] = users[ui].get('albums', []) + [album]
# # bcrypt
# File("users.json").write(users)
#
# # terminal
#
# """
# Leanne
# Romaguera
# Ervin
# Deckow
# Clementine
# Romaguera
# Patricia
# Robel
# Chelsey
# Keebler
# Mrs
# Considine
# Kurtis
# Johns
# Nicholas
# Abernathy
# Glenna
# Yost
# Yoementina
# Hoeger
#
# """
#
# name = input(">>>")  # Le -> searching : name
#
# """
# [
#     {
#       "id": 1,
#       "name": "Leanne Graham",
#       "username": "Bret"
#     }
# ]
# """
# import json

# class File:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def read(self):
#         with open(self.file_path, 'r') as f:
#             data: list[dict] = json.load(f)
#         return data
#
#     def write(self, data: list[dict]):
#         with open(self.file_path, 'w') as f:
#             json.dump(data, f, indent=3)


# users: list[dict] = File("users.json").read()
# name : str = input("search >>>").lower()
# for user in users:
#     if name in user.get("name").lower():
#         print(*list(user.values())[:3])

# f =  File("districts.json")
# districts: list[dict] = f.read()
# print(*districts , sep='\n')
# for i  in range(len(districts)):
#     del districts[i]['name_oz']
#     del districts[i]['name_ru']

# f.write(districts)

# regions : list[dict] = File("regions.json").read()
# districts : list[dict] = File("districts.json").read()
# for region in regions:
#     dist = []
#     for district in districts:
#         if district.get("region_id") == region.get("id"):
#             dist.append(district)
#     region["districts"] = dist
# File("regions.json").write(regions)


# f = File("villages.json")
# villages: list[dict] = f.read()
# for i in villages:
#     del i['name_oz']
#     del i['name_ru']
# f.write(villages)
"""
PARKING
1 soat -> 10000
users.json
    id 
    fullname
    phone
    username
    password
cars.json
    id
    name
    number
    place
    user_id
    join_at
    
histories.json
    id 
    car_id
    summ 
    join_at
    return_at
    


1) Register
    save(id , fullname , username, password)
2) Login
    login(username, password)
        1) Cars
            1) Add
            2) View
            3) Change
            4) Delete
            0) <- back
        2) Parking
            1) Place View
                [(0,0) , (0,1)],
                [(1,0) , (1,1)],
                [(2,0) , (2,1)]
                
            2) Placement car
                1) BMW
                2) Gentra
                # >>>
                [(0,0) , (0,1)],
                [(1,0) , (1,1)],
                [(2,0) , (2,1)]
                # >>> 0 1
            3) Take away
                [(0,0) , (0,1)],
                [ 🚙 , (1,1)],
                [(2,0) , (2,1)]
                # >>>
                
        3) settings
            1) change
            2) info
            0) <- back
            
        4) logout
3) exit
"""

# import json
# json - > load , dump , loads , dumps

# with open("test.json", 'r') as file:
#     data : list = json.load(file)
#     data.append(10)

# with open("test.json" , 'w') as file:
#     json.dump(data, file , indent=3)

# d = {1:1 , 2:2}
# d = json.dumps(d)
# print(type(d) , d[0])
# d = json.loads(d)
# print(type(d) , d)



