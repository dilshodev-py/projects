from DB.model import Users


class UI:
    def main(self):
        try:
            menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
            match input(menu):
                case "1":
                    user = {
                        "username" : input("username:"),
                        "password" : input("password")
                    }
                    user = Users(**user)
                    user.is_valid()
                    user.insert()
                    print("Mofaqiyatli saqlandi !")
                    self.main()
                case "2":
                    user = {
                        "username": input("username:"),
                        "password": input("password")
                    }
                    user = Users(**user).select()
                    if user:
                        print("Welcome account")

                    else:
                        print("BUnday account mavjud emas")
                    self.main()
                case "3":
                    return
        except Exception as e:
            print(e)
            self.main()

UI().main()