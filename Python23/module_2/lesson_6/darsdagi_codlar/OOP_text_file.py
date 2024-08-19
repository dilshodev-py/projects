# class File:
#
#     @classmethod
#     def read(cls):
#         file_name = cls.__name__.lower() + "s.txt"
#         with open(file_name, "r") as f:
#             data = f.read().split("\n")
#         if "" in data:
#             del data[0]
#         for i , item in enumerate(data):
#             item = item.split("|")
#             data[i] = cls(*item)
#         return data
#
#     def write(self, data: list[str]):
#         data = "\n".join(data)
#         with open(self.file_path, "w") as f:
#             return f.write(data)
#
# class User(File):
#     def __init__(self , id = None, fullname = None):
#         self.id = id
#         self.fullname = fullname
#
#
# users : list[User] = User().read()
# for user in users:
#     print(user.id)

class File:
    def read(self):
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(file_name, "r") as f:
            data = f.read().split("\n")
        if "" in data:
            del data[0]
        return data

    def write(self, data: list[str]):
        file_name = self.__class__.__name__.lower() + "s.txt"
        data = "\n".join(data)
        with open(file_name, "w") as f:
            return f.write(data)


class User(File):
    def __init__(self , id = None , fullname = None):
        self.id = id
        self.fullname = fullname


    def save(self):
        user_str = "|".join(map(str , self.__dict__.values()))
        users: list[str] = self.read()
        users.append(user_str)
        self.write(users)






User(id = 10 , fullname = "Karl").save()
