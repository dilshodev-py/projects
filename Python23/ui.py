from models import User, ToDo
from datetime import datetime

session_user: None | User = None


class UserUI:

    def settings(self):
        global session_user
        menu = """
            1) My info
            2) Edit 
            3) Delete account
            0) <-back
            >>>"""
        key = input(menu)
        match key:
            case "1":
                print(session_user.__dict__)
                self.settings()
            case "2":
                self.edit()
            case "3":
                pass
            case "0":
                UI().account()

    def edit(self):
        field = """
            1) fullname
            2) phone number
            3) password
            0) <-back
            """
        key = input(field)
        if key == 0:
            self.settings()
        new_val = input("New value: ")
        match key:
            case "1":
                User(id=session_user.id).update("fullname", new_val)
            case "2":
                User(id=session_user.id).update("phone_number", new_val)
            case "3":
                User(id=session_user.id).update("password", new_val)
        self.settings()

class UI:
    def main(self):
        global session_user
        menu = """
        ===============================Register/Login=================================
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
            "phone_number": input("Phone number : "),
            "password": input("Password : ")
        }
        user = User(**auth_user)
        is_bool, response = user.is_login()
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
            "phone_number": input("Phone : (+998) "),
            "password": input("password : "),
            "join_at": datetime.now()
        }
        user = User(**user)
        is_bool, message = user.is_valid()
        if is_bool:
            user.save()
        print(message)
        self.main()

    def account(self):
        global session_user
        menu = """
        ====================================MENU=====================================
            1) ToDo
            2) My ToDo
            3) settings
            0) logout
            >>>"""
        key = input(menu)
        match key:
            case "1":
                UI().account()
            case "2":
                UI().account()
            case "3":
                UserUI().settings()
            case "0":
                session_user = None



UI().main()
