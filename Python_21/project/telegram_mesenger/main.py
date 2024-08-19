from model.user import *
from module_2.telegram_mesenger.error import ErrorMessage
# pip install colorama

stickers = {'0': '👮♂', '1': '️🧕', '2': '👷♂', '3': '️🕵️♂', '4': '️👩⚕', '5': '️🧑⚕', '6': '️👨⚕', '7': '️👨🌾',
            '8': '👩🍳', '9': '👩🏫', '10': '👩🎓', '11': '👩💼'}

ENUM_USER_FIELD_DICT = {
            "1": "fullname",
            "2": "username",
            "3": "bio",
            "4": "photo",
            "5": "phone_number"
}

session_user : None | User = None

class UserUI:

    def sticker_show(self):
        for key, sticker in stickers.items():
            if int(key) % 2 == 0:
                print()
            print(f"{key}) {sticker}", end="          ")
        sticker_key = input(">>>")
        return stickers.get(sticker_key)

    def register(self):
        user = {
            "id": User().sequence_id(),
            "fullname": input("Fullname : "),
            "username": input("Username : "),
            "phone_number": input("Phone number : "),
            "bio": input("Bio : "),
            "photo": self.sticker_show()
        }
        user = User(**user)
        user.is_valid()
        user.save()
        UI().main()

    def login(self):
        global session_user
        auth = {
            "phone_number" : input("Phone number : ")
        }
        user = User(**auth)
        session_user = user.is_auth()
        self.account()


    def update_field(self):
        try:
            print(session_user.__dict__)
            menu = """
                1) fullname
                2) username
                3) bio
                4) photo
                5) phone_number
                0) <= back
                >>>"""
            key = input(menu)
            if key == "0":
                self.settings()
                return
            field = ENUM_USER_FIELD_DICT.get(key)
            new_val = input("New value : ")
            User(id = session_user.id).update(field, new_val)
            self.account()
        except ErrorMessage as messsage:
            print(messsage)
            self.settings()
    def settings(self):
        global session_user
        menu = """
            1) update profile
            2) delete account
            0) <-back
        """
        match input(menu):
            case "1":
                self.update_field()
            case "2":
                y_n = input("Are you sure [y/N] : ")
                if y_n == 'y':
                    User(id = session_user.id).delete()
                    session_user = None
                    UI().main()
                self.settings()
            case "0":
                self.account()

    def account(self):
        global session_user
        menu = """
            1) chats (+0)
            2) groups (+0)
            3) channels (+0)
            4) contact
            5) settings
            0) logout
        """
        match input(menu):
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                self.settings()
            case "0":
                session_user = None
                UI().main()


class UI:
    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) exits
                >>>"""

            match input(menu):
                case "1":
                    UserUI().register()
                case "2":
                    UserUI().login()
                case "3":
                    return
        except ErrorMessage as message:
            print(message)
            self.main()


UI().main()

# 16:20
