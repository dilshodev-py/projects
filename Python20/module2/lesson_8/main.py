# import json
# # loads , dumps
# # load , dump
#
# # users = [
# #     {
# #         "id": 1,
# #         "fullname": "Botir"
# #     }
# # ]
#
# l = [1,2,3]
# l  = json.dumps(l)
# print(type(l))
# l = json.loads(l)
# print(type(l))
# # with open("test.json", "r") as f:
# #     users: list[dict] = json.load(f)
# #
# # users.append(user)
# # with open("test.json" , 'w') as f:
# #     json.dump(users, f, indent=3)
#
# # File(file_name) -> read() , write()
#
# class File:
#     def __init__(self , file_path):
#         self.file_path = file_path
#
#     def read(self):
#         with open(self.file_path , 'r') as f:
#             return json.load(f)
#
#     def write(self , data : list[dict]):
#         with open(self.file_path , 'w') as f:
#             return json.dump(data, f , indent=3)
#
# user = {
#     "id" : 2,
#     "fullname" : "Kamol"
# }
#
# def add(obj):
#     f = File("test.json")
#     users = f.read()
#     users.append(obj)
#     f.write(users)
#
# def delete(id):
#     f = File("test.json")
#     users : list[dict] = f.read()
#     for i in users:
#         if i["id"] == id:
#             users.remove(i)
#     f.write(users)
import json


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path , 'r') as f:
            data: list[dict] = json.load(f)
        return data

    def write(self , data : list[dict]):
        with open(self.file_path , 'w') as f:
            json.dump(data , f , indent=3)


posts : list[dict] = File("posts.json").read()
users : list[dict] = File("users.json").read()








