# main thread


import json
from typing import Optional

from module_3.lesson_5.auth.log import user_logger, main_logger
from module_3.lesson_5.auth.utils import send_email




class File:
    def read(self):
        file_name = self.__class__.__name__.lower() + "s.json"
        with open(file_name, 'r') as f:
            try:
                data = json.load(f)
            except :
                data = []
        for i, v in enumerate(data):
            data[i] = self.__class__(**v)
        return data

    def write(self, data: list[object]):
        file_name = self.__class__.__name__.lower() + "s.json"
        for i, v in enumerate(data):
            data[i] = v.__dict__
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=3)


class User(File):
    def __init__(self,
                 id=None,
                 fullname=None,
                 phone_number=None,
                 email=None):
        self.id = id
        self.fullname = fullname
        self.phone_number = phone_number
        self.email = email

    def sequence_id(self):
        try:
            users = self.read()
            return users[-1].id + 1 if users else 1
        except Exception as error:
            main_logger.error(error)


    def save(self):
        try:
            users: list[User] = self.read()
            users.append(self)
            self.write(users)
        except Exception as error:
            main_logger.error(error)

    def is_auth(self):
        try:
            users: list[User] = self.read()
            for user in users:
                if user.phone_number == self.phone_number:
                    return user
        except Exception as error:
            main_logger.error(error)
        else:
            raise Exception(f'Not found {self.phone_number} !')


    def is_valid(self):
        try:
            users: list[User] = self.read()
            for user in users:
                if user.phone_number == self.phone_number:
                    raise Exception("Already Exists !")
        except Exception as error:
            main_logger.error(error)


session_user: Optional[User] = None


class UI:
    def main(self):
        try:
            menu = """
            1) Register
            2) login
            3) exit
            >>>"""
            match input(menu):
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as m:
            print(m)
            user_logger.error(m)
            self.main()

    def register(self):
        user = {
            "id": User().sequence_id(),
            "fullname": input("fullname:"),
            "phone_number": input("phone_number:"),
            "email": input("email:")
        }
        user = User(**user)
        user.is_valid()
        user.save()
        user_logger.info(f"Success : {user.phone_number}")
        self.main()

    def login(self):
        global session_user
        auth = {
            "phone_number": input("phone number : ")
        }
        auth = User(**auth)
        user = auth.is_auth()
        code = send_email(user.email)
        access_code = input("Code : ")
        if code != access_code:
            raise Exception("Invalid code ! Qaytadan urinib ko'r")
        session_user = user
        self.account()

    def account(self):
        global session_user
        print("=---------------------- Welcome -------------------------------=")
        print("3) logout")
        key = input(">>>")
        if key == "3":
            session_user = None
            self.main()

UI().main()





