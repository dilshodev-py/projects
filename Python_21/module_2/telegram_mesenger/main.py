from datetime import datetime

from module_2.telegram_mesenger.error import ErrorMessage
from module_2.telegram_mesenger.model.message import Message
from module_2.telegram_mesenger.model.tmp import MessageDTO, UserDTO
from module_2.telegram_mesenger.model.user import User

stickers = {'0': '👮♂', '1': '️🧕', '2': '👷♂', '3': '️🕵️♂', '4': '️👩⚕', '5': '️🧑⚕', '6': '️👨⚕', '7': '️👨🌾',
            '8': '👩🍳', '9': '👩🏫', '10': '👩🎓', '11': '👩💼'}

ENUM_USER_FIELD_DICT = {
    "1": "fullname",
    "2": "username",
    "3": "bio",
    "4": "photo",
    "5": "phone_number"
}

session_user: None | User = None


class ChatUI:
    def menu(self):
        tmp = {
            "type": "DIRECT",
            "send_user_id": session_user.id,
        }
        print("0) search")
        receivers: set[tuple] = Message(**tmp).get_receiver()
        for receiver in receivers:
            print(f"{receiver[0]}) {receiver[1]}")
        print("-1) back")
        key = input(">>>")
        match key:
            case "0":
                username = input("search username>>>")  # Bo
                User(username=username).show_users()
                message = {
                    "id": Message().sequence_id(),
                    "type": "DIRECT",
                    "send_user_id": session_user.id,
                    "to_receiver_id": input("Receiver >>>"),
                    "message": input("message >>>"),
                    "date_time" : str(datetime.now())
                }
                Message(**message).save()
                self.menu()
                return
            case "-1":
                UserUI().account()
                return
        self.chat(key)


    def build_chat(self, messages , send_user_id):
        for message in messages:
            if message.send_user_id == send_user_id:
                print( f"{' ' * 30}{message.send_user_id}: {message.message}")
            else:
                print(f"{' '}{message.send_user_id}: {message.message}")



    def chat(self, receiver_id):
        session_message: list[MessageDTO] = Message(to_receiver_id=receiver_id, send_user_id=session_user.id).get_chat()
        receiver_message: list[MessageDTO] = Message(to_receiver_id=session_user.id,
                                                     send_user_id=receiver_id).get_chat(receiver = True)
        session_message.extend(receiver_message)
        session_message.sort(key=lambda x: datetime.fromisoformat(x.date_time))

        self.build_chat(session_message, session_user.id)
        message = {
            "id": Message().sequence_id(),
            "type": "DIRECT",
            "send_user_id": session_user.id,
            "to_receiver_id": receiver_id,
            "message": input("Message[end] >>>"),
            "date_time" : str(datetime.now())
        }
        if message.get("message").lower() == "end":
            self.menu()
            return
        Message(**message).save()
        self.chat(receiver_id)


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
        try:
            global session_user
            auth = {
                "phone_number": input("Phone number : ")
            }
            user = User(**auth)
            session_user = user.is_auth()
            self.account()
        except ErrorMessage as message:
            print(message)
            UI().main()

    def update_field(self):
        global session_user
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
        session_user = User(id=session_user.id).update(field, new_val)
        self.account()

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
                    User(id=session_user.id).delete()
                    session_user = None
                    UI().main()
                self.settings()
            case "0":
                self.account()

    def account(self):
        global session_user
        c = Message(send_user_id=session_user.id).unread_message()
        menu = f"""
            1) chats (+{c})
            2) groups (+0)
            3) channels (+0)
            4) contact
            5) settings
            0) logout
        """
        match input(menu):
            case "1":
                ChatUI().menu()
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
