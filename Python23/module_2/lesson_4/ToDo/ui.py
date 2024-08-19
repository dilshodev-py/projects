from models import User, ToDo
from datetime import datetime

session_user: None | User = None


class UserUI:
    def settings(self):
        menu = """
            1) My info
            2) Edit 
            3) Delete account
            0) <-back
            >>>"""
        key = input(menu)
        pass

    def edit(self):
        field = """
            1) fullname
            2) phone number
            3) password
            0) <-back
            """
        key = input(field)
        pass


class UI:
    def main(self):
        menu = """
            1) Register
            2) Login
            3) exit
            >>>"""
        key = input(menu)
        pass

    def login(self):
        auth_user = {
            "phone_number": input("Phone number : "),
            "password": input("Password : ")
        }
        pass

    def register(self):
        user = {
            "id": "id",
            "fullname": input("Fullname : "),
            "phone_number": input("Phone : (+998) "),
            "password": input("password : "),
            "join_at": "datetime"
        }
        pass

    def account(self):
        menu = """
            1) ToDo
            2) My ToDo
            3) settings
            0) logout
            >>>"""
        key = input(menu)



UI().main()

# 16:20
