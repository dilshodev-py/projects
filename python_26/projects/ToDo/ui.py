from typing import Optional

from projects.ToDo.backend import User
from projects.ToDo.exceptions import AuthException

session_user: Optional[User] = None


class TodoUI:
    def todo_page(self):
        menu = """
          *) 🔎 search
          1) todos
          2) add
          0) back
          >>>"""
        match input(menu):
            case "*":
                pass
            case "1":
                pass
            case "2":
                pass
            case "0":
                AccountUI().account_page(back=True)

    def todos_list_page(self):
        pass

    def todo_add_page(self):
        pass


class AccountUI(TodoUI):
    def settings_page(self):
        menu = """
          1) About
          2) Edit account
          3) Delete account
          0) back
          >>>"""
        match input(menu):
            case "1":
                text = f"""
                     Fullname : {session_user.first_name} {session_user.last_name}
                     email :    {session_user.email}
                     password : {session_user.password}
                """
                print(text)
                input("Click Enter with back !")
                self.settings_page()
            case "2":
                fields = {
                    '1': "first_name",
                    '2': "last_name",
                    '3': "email",
                    '4': "password",
                }
                menu = """
                     *) full edit
                     1) first name
                     2) last name
                     3) email
                     4) password
                     0) back
                     >>>"""
                key = input(menu)
                if key == "*":
                    pass
                elif key == "0":
                    self.settings_page()
                else:
                    field = fields[key]
                    new_value = input("New Value>>>")
                    User(id=session_user.id).update(field=field, new_value=new_value)
                self.settings_page()

            case "3":
                session_user.delete()
                UI().main()
            case "0":
                self.account_page(back=True)

    def account_page(self, back=False):
        global session_user
        if not back:
            print(f"Welcome to ToDo ! {session_user.first_name} {session_user.last_name}")
        menu = """
        1) Todo
        2) settings
        0) logout
        >>>"""
        match input(menu):
            case "1":
                self.todo_page()
            case "2":
                self.settings_page()
            case "0":
                UI().main()


class UI(AccountUI):
    def main(self):
        try:

            menu = """
                1) Register
                2) Login
                3) exit
                >>>"""
            match input(menu):
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except AuthException as e:
            print(e)
            self.main()

    def register(self):
        user = {
            "first_name": input("first_name:".title()),
            "last_name": input("last_name:".title()),
            "email": input("email:".title()),
            "password": input("password:".title()),
        }
        user = User(**user)
        user.is_valid()
        user.save()
        self.main()

    def login(self):
        global session_user
        auth = {
            'email': input("email:"),
            'password': input("email:"),
        }
        auth = User(**auth)
        session_user = auth.is_auth()
        self.account_page()




UI().main()
