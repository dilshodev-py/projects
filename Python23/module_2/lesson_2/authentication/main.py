from datetime import datetime

users: list['User'] = []


class User:
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 phone: str = None,
                 username: str = None,
                 password: str = None,
                 join_at: str = None,
                 ):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.username = username
        self.password = password
        self.join_at = join_at

    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def save(self):
        users.append(self)

    def is_valid(self):
        if len(self.phone) != 13:
            return False, 'Invalid phone number !'
        if len(self.password) < 4:
            return False, "Invalid password !"
        is_bool, message = self.is_username()
        if not is_bool:
            return is_bool, message
        return is_bool, message

    def is_username(self):
        for user in users:
            if user.username == self.username:
                return False, "Already exists Username !"

        return True, "Success !"

    def is_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return True, user
        return False, "Not found account !"

session_user: None | User = None

class UI:

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


    def login(self):
        auth = {
            "username": input("Username: "),
            "password": input("Password : ")
        }
        user = User(**auth)
        is_bool, response = user.is_login()
        if is_bool:
            session_user = response
            self.account()
            return
        print(response)

    def account(self):
        print(f"Welcome ! {session_user.fullname}")

    def main(self):
        menu = """
            1) Register
            2) Login
            3) exit
            >>>"""
        key = input(menu)
        # if key == "1":
        #     pass
        # elif key == "2":
        #     pass
        # elif key == "3":
        #     return
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                print("Finished !")
                return


UI().main()
