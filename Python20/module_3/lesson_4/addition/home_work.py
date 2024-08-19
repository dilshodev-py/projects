import logging
import json
import os

# logger
register_info_logger = logging.getLogger("user_info")
register_debug_logger = logging.getLogger("user_debug")
error_logger = logging.getLogger("project")
register_debug_logger.setLevel(logging.DEBUG)
register_info_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.ERROR)

# handler
info_handler = logging.FileHandler("user_info.log")
debug_handler = logging.FileHandler("user_debug.log")
error_handler = logging.FileHandler("error.log")

# format
for_ = '%(name)s - %(levelname)s - %(message)s - %(asctime)s'
format = logging.Formatter(for_)
info_handler.setFormatter(format)
debug_handler.setFormatter(format)
error_handler.setFormatter(format)

# add
register_info_logger.addHandler(info_handler)
register_debug_logger.addHandler(debug_handler)
error_logger.addHandler(error_handler)

# level
info_handler.setLevel(logging.INFO)
debug_handler.setLevel(logging.DEBUG)
error_handler.setLevel(logging.ERROR)


class Logging:
    def __init__(self , level , message):
        self.level = level
        self.message = message

    def strim(self):
        logging.basicConfig(level=self.level , format=for_)
        if self.level == 0:
            logging.debug(self.message)
        if self.level == 1:
            logging.info(self.message)
        if self.level == 3:
            logging.error(self.message)
    def file_log(self):
        if self.level == 0:
            register_debug_logger.debug(self.message)
        if self.level == 1:
            register_info_logger.info(self.message)
        if self.level == 3:
            error_logger.error(self.message)


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path , "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            log = Logging(3, f"{__file__} -> {e}")
            log.file_log()
            return []


    def write(self, data):
        with open(self.file_path , "w") as f:
            json.dump(data, f, indent=3)



class User:
    def __init__(self ,
                 username = None,
                 password = None):
        self.username = username
        self.password = password

    def is_valid(self):
        file = File("user.json")
        users = file.read()

        for user  in users:
            if user.get("username") == self.username:
                log = Logging(0, f"Already username -> {self.username}")
                log.file_log()
                raise Exception("Already exits username")


    def save(self):
        file = File("user.json")
        data= file.read()
        data.append(self.__dict__)
        file.write(data)
        log = Logging(1 , f"Save -> {self.username}({self.password})")
        log.file_log()

    def is_login(self):
        file = File("user.json")
        users = file.read()
        for user in users:
            if user.get("username") == self.username and user.get("password") == self.password:
                log = Logging(1 , f"Enter account -> {self.username}")
                log.file_log()
                return user
        log = Logging(0 , f"Login Failed {self.username}({self.password})")
        log.file_log()
        raise Exception("Login Failed")



while True:
    menu = """
        1) Login
        2) Register
        >>>"""
    key = input(menu)
    try:
        match key:
            case "1":
                user = {
                    "username" : input("Username : "),
                    "password" : input("Password : ")
                }
                User(**user).is_login()
            case "2":
                user = {
                    "username": input("Username : "),
                    "password": input("Password : ")
                }
                user = User(**user)
                user.is_valid()
                user.save()
    except Exception as e:
        print(e)
        continue









