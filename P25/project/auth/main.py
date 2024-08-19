users: list['User'] = []


class User:
    def __init__(self, id: int = None,
                 fullname: str = None,
                 username: str = None,
                 password: str = None):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def save(self):
        users.append(self)

    def is_valid(self):
        for user in users:
            if user.username == self.username:
                return (False, "Already exists username")
        if len(self.password) < 4:
            return (False, "Password uzunligi 4 dan kichkina")

        return (True, "Success")

    def is_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return (True, user)
        return (False, "Not found account !")


class UI:

    def register(self):
        fullname = input("Fullname :")
        username = input("Username :")
        password = input("Password :")
        user = {
            "id": User().sequence_id(),
            "fullname": fullname,
            "username": username,
            "password": password
        }

        # User(id = user.get("id") , fullname = user.get("fullname"))
        user = User(**user)
        is_valid, message = user.is_valid()
        if is_valid == True:
            users.append(user)
        print(message)
        self.main()

    def login(self):
        auth = {
            "username": input("Username: "),
            "password": input("Password: "),
        }
        user = User(**auth)
        is_auth, response = user.is_login()
        if is_auth == True:
            print(f"Welcome {response.fullname} to account")
            return
        print(response)
        self.main()

    def main(self):
        menu = """
            1) register
            2) login
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


UI().main()

# FOCUS

# Umar
# Ruhsorbek
# Behruz
# Musavvir
# Sardor
# Yulduz
# Hojiakbar
# Shohruz
# Behruz Ismoilov
# Bobomurod
# Adolat
# Iskandar
# Sarvinoz




