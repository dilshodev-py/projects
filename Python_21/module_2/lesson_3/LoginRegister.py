
"""
User
    id
    fullname
    username
    password
    join_date
"""
from datetime import date

users: list[dict] = []
class Base:
    def __init__(self , data :list):
        self.data = data

    def sequence_id(self):
        return self.data[-1].get("id") + 1 if self.data else 1

class User(Base):
    def __init__(self,
                 id = None ,
                 fullname = None ,
                 username = None ,
                 password = None,
                 join_date = None,
                 data = None):
        super().__init__(data)
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password
        self.join_date = join_date

    def check_username(self):
        for user in self.data:
            if user.get("username") == self.username:
                return False,"Already exits username"
        return True,"Success"

    def is_login(self):
        for user in self.data:
            if user.get("username") == self.username and user.get("password") == self.password:
                return True
        return False

    def save(self):
        user = self.__dict__
        del user["data"]
        users.append(user)

class UI:

    def register(self):
        print("================ REGISTER ==================")

        user = {
            "id" : User(data=users).sequence_id(),
            "fullname" : input("Fullname : "),
            "username" : input("Username : "),
            "password" : input("Password : "),
            "join_date" : date.today()
        }
        user = User(**user, data=users)
        response: tuple = user.check_username()
        if response[0]:
            user.save()

        print(response[1])
        self.main()

    def login(self):
        print("================ LOGIN ==================")
        user = {
            "username" : input("Username : "),
            "password" : input("Password : ")
        }
        user = User(**user , data = users)
        response : bool = user.is_login()
        if not response:
            print("Not found account :(")
            self.main()
            return
        self.account()

    def account(self):
        print("WELCOME !")

    def main(self):
        menu = """
            1) Register
            2) Login
            3) Exits
            >>>"""
        key: str = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return


UI().main()

"""
 1) Register
    Fullname>>>
    username>>>
    password>>>
    check(username)
    
 2) Login
    Username >>>
    Password >>>
    check(username and password)
    print("Welcome account")
 3) exit
 >>>1
"""
