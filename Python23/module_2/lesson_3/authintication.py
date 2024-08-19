from datetime import datetime

users: list['User'] = []


class User:
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 phone: str = None,
                 username: str = None,
                 password: str = None,
                 join_at: str = None):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.username = username
        self.password = password
        self.join_at = join_at

    def is_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return True, user
        return False, "Not found Account :("

    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def save(self):
        users.append(self)

    def is_exist_username(self):
        for user in users:
            if user.username == self.username:
                return False, "Already exist username :("
        return True, "Success"

    def is_valid(self):
        if len(self.phone) != 13:
            return False, "Invalid Phone number"
        if len(self.password) < 4:
            return False, "Invalid Password"
        return self.is_exist_username()


session_user: None | User = None


class UI:
    def main(self):
        menu = """
            1) Register
            2) Login
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

    def login(self):
        global session_user
        auth_user = {
            "username": input("Username : "),
            "password": input("Password : ")
        }
        auth_user = User(**auth_user)
        is_bool, response = auth_user.is_login()
        if is_bool:
            session_user = response
            self.account()
            return
        print(response)
        self.main()

    def register(self):
        user = {
            "id": User().sequence_id(),
            "fullname": input("Fullname : "),
            "phone": input("Phone : "),
            "username": input("Username : "),
            "password": input("Password : "),
            "join_at": str(datetime.now())
        }
        user = User(**user)
        is_bool, message = user.is_valid()
        if is_bool:
            user.save()
        print(message)
        self.main()

    def account(self):
        print("Welcome :)")

UI().main()

# 15:43
