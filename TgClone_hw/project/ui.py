from typing import Optional

from project.user import User
from utils import choose_emoji

"ctrl+2*space"
current_user : Optional[User] = None
class UI:
    def main(self):
        menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
        match input(menu):
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

    def register(self):
        user = {
            "id" : User().sequence_id(),
            "phone_number": input("phone_number : "),
            "first_name" : input("first_name : "),
            "last_name": input("last_name : "),
            "username" : input("username : "),
            "photo" : choose_emoji(),
            "bio" : input("bio : "),
        }
        user = User(**user)
        is_bool , message = user.is_valid()
        if is_bool:
            user.save()
        print(message)
        self.main()



    def login(self):
        global current_user
        auth = {
            "phone_number" : input("phone_number : ")
        }
        user = User(**auth)
        is_login , response = user.is_login()
        if is_login:
            current_user = response
            self.account()
            return
        print(response)
        self.main()



    def account(self):
        print(f"Welcome {current_user.first_name} {current_user.last_name}")
