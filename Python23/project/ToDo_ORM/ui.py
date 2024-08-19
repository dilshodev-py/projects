from project.ToDo_ORM.DB.DTO import UserDTO
from project.ToDo_ORM.config import send_email_code
from project.ToDo_ORM.models.auth import User
session_user: None | tuple = None

class UI:
    def register(self):
        user = {
            "first_name" : input("first_name"),
            "last_name" : input("last_name"),
            "email" : input("email"),
        }
        UserDTO(**user).save()
        self.main()

    def login(self):
        global session_user
        auth = {
            "email" : input("email:")
        }
        user:tuple  = User().select(**auth)[0]
        code = send_email_code(user[3])
        valid_code = int(input("Code :"))
        if code != valid_code:
            raise Exception("Invalid code")
        session_user = user
        self.account()

    def account(self):
        print(f"---------- Welcome {session_user[1]}")

    def main(self):
        try:
            menu = """
                1) Register
                2) login
                3) exit
                >>>"""
            match input(menu):
                case '1':
                    self.register()
                case '2':
                    self.login()
                case '3':
                    return
        except Exception as e:
            print(e)
            self.main()