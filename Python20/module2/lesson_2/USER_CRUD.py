# a = [1,2,3,4,10,9]
# print(id(a))
# a[-2] , a[-1] = a[-1] , a[-2]
# print(a)
# print(id(a))


# d = {
#     "key1": {
#         "sub_key": 10,
#         "name" : "John"
#     },
#     "key2": {
#         "sub_key": 20
#     }
# }


# c = 0
# def sub_dict(dict_):
#     global c
#     c += len(dict_)
#     for i in dict_.values():
#         if isinstance(i, dict):
#             sub_dict(i)
#     return c
# print(sub_dict(d))


# summ = 0
# for i in d.values():
#     summ += i.get('sub_key')
# print(summ)
# x = 9
# y = 10
# def a():
#     global x,y
#     x = 10
#     y = 9
#
# a()
# print(y)


users : list['User'] = []

class User:
    def __init__(self,
                 id: int,
                 fullname: str,
                 phone: str,
                 email: str,
                 role: str,
                 join_at: str,
                 ):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.role = role
        self.join_at = join_at

    def save(self):
        users.append(self)

    def delete(self):
        for i , user in enumerate(users):
            if user.id == self.id:
                del users[i]


def main():
    menu = """
    1) Account create
    2) Account edit
    3) Account list
    4) Account delete
    >>>"""
    key = input(menu)
    if key == "1":
        user = {
            "id" : users[-1].id + 1 if users else 1,
            "fullname" : input("Fullname : "),
            "phone" : input("Phone : "),
            "email" : input("Email : "),
            "role" : input("Role : "),
            "join_at" : input("Join at : ")
        }
        user_obj = User(**user)
        user_obj.save()
        print("Success register")
        print("__________________________________")

        main()

    if key == "3":
        for user in users:
            print(user.__dict__)
        print("__________________________________")
        main()

    if key == "2":
        id = int(input("id : "))
        for user in users:
            if user.id == id:
                find_user = user
                print(user.__dict__)
        fields = """
        1) Fullname
        2) Phone
        3) Email
        4) Role
        >>>"""
        key = input(fields)
        new_val = input("New value : ")
        if key == "1":
            find_user.fullname = new_val
        if key == "2":
            find_user.phone = new_val
        if key == "3":
            find_user.email = new_val
        if key == "4":
            find_user.role = new_val
        print("__________________________________")
        main()

    if key == "4":
        id = int(input("Id :"))
        for i , user in enumerate(users):
            if user.id == id:
                del users[i]
        print("________________________________")
        main()

main()
"""
Create
Read
Update
Delete
"""











# user = {
#     "id": 1,
#     "fullname": "Botir",
#     "phone": "+99891234567",
#     "email": "botir@gmail.com",
#     "role": "ADMIN",
#     "join_at": "2023-12-07"
# }

# user1 = User(**user)
# user1.save()
#
# for i in users:
#     if i.id == 1:
#         i.role = "USER"
#
# print(user1.role)






# user1 = User(**user)
# user1.save()
# print(users)
# for i in users:
#     print(i.id)
# user1.delete()
# print(users)
# user1.save()
# print(users)



# user1 = {
#     "id": 2,
#     "fullname": "John",
#     "phone": "+99891234567",
#     "email": "John@gmail.com",
#     "role": "ADMIN",
#     "join_at": "2023-12-07"
# }
# user2 = {
#     "id": 3,
#     "fullname": "Polat",
#     "phone": "+99891234567",
#     "email": "Polat@gmail.com",
#     "role": "ADMIN",
#     "join_at": "2023-12-07"
# }

# user_obj = User(
#     id = user.get("id"),
#     fullname = user.get("fullname"),
#     phone = user.get("phone"),
#     email = user.get("email"),
#     role = user.get("role"),
#     join_at = user.get("join_at"),
# )

# user_obj = User(**user)
# user_obj1 = User(**user1)
# user_obj2 = User(**user2)
# user_obj.save()
# user_obj1.save()
# user_obj2.save()

# for i in users:
#     if i.fullname.startswith("B"):
#         i.save()

