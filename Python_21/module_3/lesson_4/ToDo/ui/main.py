import datetime

from module_3.lesson_4.ToDo.config import send_email_code, user_logger
from module_3.lesson_4.ToDo.errors.main import ErrorMessage
from module_3.lesson_4.ToDo.model.user import User

session_user: None | User = None

class UserUI:
    async def register(self):
        user_dict = {
            "id" : await User().sequence_id(),
            "fullname" : input("Fullname : "),
            "email" : input("Email [your@gmail.com] : "),
            "password" : input("password : "),
            "join_at" : str(datetime.datetime.now())
        }
        user: User = User(**user_dict)
        await user.is_valid()
        code = await send_email_code(user.email)
        session_code = input("Email confirm code :")
        if session_code != str(code):
            user_logger.warning(f"Wrong Code {user.email}")
            raise ErrorMessage("Wrong Code ")
        await user.save()
        await UI().main()

    async def login(self):
        global session_user
        user_dict = {
            "email": input("Your Email : "),
            "password": input("password : ")
        }
        user: User = User(**user_dict)
        session_user = await user.is_auth()
        await self.account()
    async def account(self):
        print("Welcome !")
        print("0) logout")
        key = input(">>>")
        if key == "0":
            await UI().main()

class UI:
    async def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) Exit
                >>>"""
            key = input(menu)
            match key:
                case "1":
                    await UserUI().register()
                case "2":
                    await UserUI().login()
                case "3":
                    return
        except ErrorMessage as m:
            print(m)
            await self.main()

class ToDoUI:
    pass
















