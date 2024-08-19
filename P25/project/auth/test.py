"""
auth:
    login
    register
"""

"""
User:
    id
    fullname
    username
    password
"""

users :list['User'] = []
class User:
    def __init__(self ,
                 id : int = None,
                 fullname : str = None,
                 username : str = None,
                 password : str = None):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def save(self):
        users.append(self)

    def is_valid(self):
        # username unique
        # password >= 4
        for user in users:
            if user.username == self.username:
                return (False , "Already exists username !")
        if len(self.password) < 4:
            return (False, "Passwordni uzunligi 4 dan kichik")
        return (True , "Success")

    def is_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return (True , user)
        return (False , "Not found !")



class UI:

    def register(self):
        user = {
            "id" : User().sequence_id(),
            "fullname" : input("Fullname : "),
            "username" : input("Username : "),
            "password" : input("Password  :")
        }
        user = User(**user)
        is_valid , message = user.is_valid()
        if is_valid == True:
            user.save()
        print(message)
        self.main()

    def login(self):
        login_field = {
            "username" : input("Username : "),
            "password" : input("Password : ")
        }
        user = User(**login_field)
        is_exists , response = user.is_login()
        if is_exists == True:
            print(f"Welcome {response.fullname}")
        print(response)
        self.main()
    def main(self):
        menu = """
            1) register
            2) login
            3) exit
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

UI().main()









