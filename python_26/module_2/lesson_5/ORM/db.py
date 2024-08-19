# {
#     "id" : 1,
#     "first_name" : 'Kamol',
#     "last_name" : 'Komilov',
#     "age" : 25,
# }


class DB:
    @property
    def get_data(self) -> list:
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(file_name, 'r') as f:
            readlines = f.readlines()

        res = []
        for data in readlines:
            res.append(self.__class__(*data.rstrip('\n').split('|')))
        return res

    def save(self, data: list):
        file_name = self.__class__.__name__.lower() + "s.txt"

        data = "\n".join(["|".join(map(str ,i.__dict__.values())) for i in data])
        with open(file_name, 'w') as f:
            f.write(data)


class User(DB):
    def __init__(self, id=None, first_name=None, last_name=None, age=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Product(DB):
    def __init__(self, id=None, name=None, price=None):
        self.id = id
        self.name = name
        self.price = price


# new_user = User(3 , 'Farhod' , 'Farhodov' , 25)
# users: list[User] = User().get_data
# print(users)
# # users.append(new_user)
# # User().save(users)

# structure


