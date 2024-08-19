import datetime

from module_3.lesson_4.ToDo.config import send_email_code, user_logger
from module_3.lesson_4.ToDo.errors.main import ErrorMessage
from module_3.lesson_4.ToDo.model.user import User

session_user: None | User = None

class UserUI:
    def register(self):
        user_dict = {
            "id" : User().sequence_id(),
            "fullname" : input("Fullname : "),
            "email" : input("Email [your@gmail.com] : "),
            "password" : input("password : "),
            "join_at" : str(datetime.datetime.now())
        }
        user: User = User(**user_dict)
        user.is_valid()
        code = send_email_code(user.email)
        session_code = input("Email confirm code :")
        if session_code != str(code):
            user_logger.warning(f"Wrong Code {user.email}")
            raise ErrorMessage("Wrong Code ")
        user.save()
        UI().main()

    def login(self):
        global session_user
        user_dict = {
            "email": input("Your Email : "),
            "password": input("password : ")
        }
        user: User = User(**user_dict)
        session_user = user.is_auth()
        self.account()
    def account(self):
        print("Welcome !")
        print("0) logout")
        key = input(">>>")
        if key == "0":
            UI().main()

class UI:
    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) Exit
                >>>"""
            key = input(menu)
            match key:
                case "1":
                    UserUI().register()
                case "2":
                    UserUI().login()
                case "3":
                    return
        except ErrorMessage as m:
            print(m)
            self.main()

class ToDoUI:
    pass




















