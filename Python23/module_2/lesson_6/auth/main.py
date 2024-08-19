"""

user
    id
    fullname
    phone
    password
"""

class File:
    def read(self):
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(file_name, "r") as f:
            data = f.read().split("\n")
        if "" in data:
            del data[0]
        return data

    def write(self, data: list[str]):
        file_name = self.__class__.__name__.lower() + "s.txt"
        data = "\n".join(data)
        with open(file_name, "w") as f:
            return f.write(data)


class User(File):
    def __init__(self, id=None, fullname=None , phone = None , password = None):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.password = password

    def sequence_id(self):
        users = self.read()
        return int(users[-1].split("|")[0]) + 1 if users else 1
    def save(self):
        user_str = "|".join(map(str, self.__dict__.values()))
        users: list[str] = self.read()
        users.append(user_str)
        self.write(users)

    def is_unique_phone(self):
        users: list[str] = self.read()
        for user in users:
            user = user.split('|')
            if user[2] == self.phone:
                return False , "Already exits phone"
        return True , "Success!"

    def is_valid(self):
        if len(self.password) < 4:
            return False , "Invalid Password"
        return self.is_unique_phone()

    def is_login(self):
        users = self.read()
        for user in users:
            user = user.split("|")
            if user[2] == self.phone and user[3] == self.password:
                return True , user
        return False , "Not Found Account !"


session_user : None | list  = None

class UI:

    def register(self):
        user = {
            "id" : User().sequence_id(),
            "fullname" : input("Fullname : "),
            "phone" : input("Phone : "),
            "password" : input("Password : ")
        }
        user = User(**user)
        is_bool , message = user.is_valid()
        if is_bool:
            user.save()
        print(message)
        self.main()

    def account(self):
        print(f"Welcome {session_user[1]}")
    def login(self):
        global session_user
        auth  = {
            "phone" : input("Phone : "),
            "password" : input("Password : ")
        }
        auth = User(**auth)
        is_bool , response = auth.is_login()
        if is_bool:
            session_user = response
            self.account()
            return
        print(response)
        self.main()
    def main(self):
        menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

UI().main()


# leetcode -
