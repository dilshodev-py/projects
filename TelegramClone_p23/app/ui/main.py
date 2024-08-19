from app.errors.main import UserValidError
from app.model.contact import Contact
from app.model.user import User
from app.utils.main import send_code

session_user: None | User = None


class Tg:

    def add_contact(self):
        username_search = input("Username search 🔎 : ")
        users: list[User] = User().search_users(username_search)
        for user in users:
            print(f"{user.id}) {user.username}")
        print("0) <-back")
        key = input(">>>")
        if key == "0":
            self.contact()
        user_id = key
        contact = {
            "id" : Contact().sequence_id,
            "user_id" :user_id,
            "owner_id" : session_user.id
        }
        Contact(**contact).save()
        self.contact()

    def contact(self):
        print("*) search account")
        user_list: list[User] = Contact(owner_id=session_user.id).owner_contact_list()
        for pos , user in enumerate(user_list,1):
            print(f"{pos}) {user.username}")
        print("0) < -back")
        key = input(">>>")
        if key == "0":
            self.account()
        if key == "*":
            self.add_contact()
            return
        choose_contact: User = user_list[int(key)-1]
        print(" "*10 , f"Fullname : {choose_contact.fullname}")
        print(" "*10 , f"Phone number : {choose_contact.phone_number}")
        self.contact()


    def account(self):
        print("-" * 10, "Menu", "-" * 10)
        menu = """
            1) chat (+0)
            2) group (+0)
            3) channel (+0)
            4) contact
            5) settings
            0) logout
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.chat()
            case "2":
                self.group()
            case "3":
                self.channel()
            case "4":
                self.contact()
            case "5":
                self.settings()
            case "0":
                UI().main()

    def settings(self):
        global session_user
        menu = """
            1) change
            2) delete account
            0) <- back
            >>>"""
        key = input(menu)
        match key:
            case "1":
                pass
            case "2":
                User(id=session_user.id).delete()
                session_user = None
                UI().main()
            case "0":
                self.account()


class UI:

    def register(self):
        account = {
            "id": User().sequence_id,
            "fullname": input("fullname : ".title()),
            "phone_number": input("phone_number : ".title()),
            "username": input("username : ".title()),
            "photo": input("photo : ".title()),
            "bio": input("bio : ".title())
        }
        access_code = send_code()
        code = input("Send Code to phone number: ")
        if access_code != code:
            raise UserValidError("Invalid Code !")
        user = User(**account)
        user.is_valid()
        user.save()
        self.main()

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
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except UserValidError as m:
            print(m)
            self.main()

    def login(self):
        global session_user
        auth = {
            "phone_number": input("Phone number : ")
        }
        auth = User(**auth)
        session_user = auth.is_login
        access_code = send_code()
        code = input("Send your phone number code : ")
        if access_code != code:
            raise UserValidError("Invalid code !")

        Tg().account()
