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
        with open(file_name , 'r') as f:
            data = f.read().split("\n")
            if "" in data:
                # del data[0]
                data.remove("")
            return data

    def write(self, data: list[str]):
        data = "\n".join(data)
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(file_name, 'w') as f:
            f.write(data)


class User(File):
    def __init__(self, id=None, fullname=None , phone = None , password = None):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.password = password

    def sequence_id(self):
        users = self.read()
        return int(users[-1].split('|')[0]) + 1 if users else 1

    def save(self):
        user_str = "|".join(map(str , self.__dict__.values()))
        users = self.read()
        users.append(user_str)
        self.write(users)
    def is_unique_phone(self):
        users = self.read()
        for user in users:
            user = user.split('|')
            if user[2] == self.phone:
                raise UserException("Already phone exists")


    def is_valid(self):
        if len(self.password) < 4:
            raise UserException("Invalid password")
        self.is_unique_phone()


    def is_login(self):
        users = self.read()
        for user in users:
            user = user.split('|')
            if user[2] == self.phone and user[3] == self.password:
                return user
        raise UserException("Not Found account !")


session_user : None | list  = None


class UserException(Exception):
    def __init__(self, message):
        Exception(self).__init__(message)

class UI:

    def register(self):
        user = {
            "id" : User().sequence_id(),
            "fullname" : input("Fullname : "),
            "phone" : input("Phone : "),
            "password" : input("Password : ")
        }
        user = User(**user)
        user.is_valid()
        user.save()
        self.main()

    def account(self):
        print(f"Welcome {session_user[1]}")
    def login(self):
        global session_user
        is_admin = input("Is Admin [yes/No]>>>")
        if is_admin == "yes":
            is_admin = True
        is_admin = False

        auth  = {
            "phone" : input("Phone : "),
            "password" : input("Password : ")
        }
        auth = User(**auth)
        session_user = auth.is_login()
        self.account()

    def main(self):
        menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
        key = input(menu)
        try:
            match key:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except UserException as message:
            print(message)
            self.main()

UI().main()

# Time ->
# 16:20


