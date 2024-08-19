from models.DTO import UserDTO
from models.model import User
from utils.main import send_code

sticker = {1: '🤠', 2: '👮', 3: '💂\u200d♂', 4: '️👨\u200d🌾', 5: '👩\u200d🏭', 6: '👩\u200d💼', 7: '👩\u200d🏫',
           8: '👩\u200d🍳', 9: '🧑\u200d⚕', 10: '️👨\u200d⚕'}


def show_sticker():
    for key, value in sticker.items():
        print(f"{key}) {value}")
    key = int(input(">>>"))
    return sticker[key]


class UI:

    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) exit
                >>>"""
            key = input(menu)
            match key:
                case "1":
                    UserUI().register()
                case "2":
                    UserUI().login()
                case "3":
                    return
        except Exception as message:
            print(message)
            self.main()


session_user: UserDTO | None = None


class UserUI:
    def register(self):
        user = {
            "fullname": input("Fullname : "),
            "phone_number": input("Phone number : "),
            "username": input("Username : "),
            "bio": input("Bio : "),
            "photo": show_sticker()
        }
        user = User(**user)
        user.is_unique_valid()
        user.save()
        UI().main()

    def login(self):
        global session_user
        phone_number = input("Phone number : ")
        user = User(phone_number=phone_number).is_login()
        access_code = send_code()
        code = input("Code : ")
        if code != access_code:
            raise Exception("Code wrong !")
        session_user = user
        self.account()

    def account(self):
        print(f"Welcome {session_user.fullname}")


class GroupUI:
    pass


class ChannelUI:
    pass


class ChatUI:
    pass


UI().main()
