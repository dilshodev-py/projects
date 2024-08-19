# users: list['User'] = []


# class User:
#     def __init__(self,
#                  id: int = None,
#                  fullname: str = None,
#                  username: str = None,
#                  password: str = None
#                  ):
#         self.id = id
#         self.fullname = fullname
#         self.username = username
#         self.password = password
#
#     def sequence_id(self):
#         if len(users) == 0:
#             return 1
#         else:
#             return users[-1].id + 1
#
#     def is_valid(self):
#         for user in users:
#             if user.username == self.username:
#                 return False, "Already exists username"
#
#         if len(self.password) < 4:
#             return False, "Password invalid"
#
#         return True, "Success"
#
#     def save(self):
#         users.append(self)
#
#     def is_login(self):
#         for user in users:
#             if user.username == self.username and user.password == self.password:
#                 return True, user
#         return False, "Not found account"
#
#
# class UI:
#     def main(self):
#         menu = """
#             1) Register
#             2) Login
#             3) Exit
#             >>>"""
#         key = input(menu)
#         match key:
#             case "1":
#                 self.register()
#             case "2":
#                 self.login()
#             case "3":
#                 return
#
#
#     def register(self):
#         user_dict = {
#             "id" : User().sequence_id(),
#             "fullname" : input("Fullname : "),
#             "username" : input("Username : "),
#             "password" : input("Password : "),
#         }
#
#         user = User(**user_dict)
#         is_valid , message = user.is_valid()
#         if is_valid == True:
#             user.save()
#         print(message)
#         self.main()
#
#
#
#     def login(self):
#         auth = {
#
#             "username" : input("Username : "),
#             "password" : input("Password : "),
#         }
#         user = User(**auth)
#         is_auth , response = user.is_login()
#         if is_auth == False:
#             print(response)
#             self.main()
#         else:
#             print(f"Welcome {response.fullname}")
#
#
#
# UI().main()


