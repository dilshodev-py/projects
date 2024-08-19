from projects.PointOfSale.app.backend import User
ADMIN_PHONE_NUMBER= "+998999999999"
ADMIN_PASSWORD= 1



class UI:

    def admin_page(self):
        print('Welcome Admin Page')
    def account(self):
        print("Account !")
    def login_page(self):
        auth = {
            "phone_number" : input('Phone Number :')
        }

        user = User(**auth)
        user = user.get()
        if user.role == 'admin':
            password = input("Password : ")
            if user.password == password:
                self.admin_page()
                return
            else:
                print("Password invalid !")
                self.main()
                return

        response = user.exists()
        if isinstance(response , bool):
            if response:
                auth['password'] = input('New password>>>'),
                auth['first_name'] = input('New first_name>>>'),
                auth['last_name'] = input('New last_name>>>'),
                User(**auth).save()
                self.main()
                return
            else:
                auth['password'] = input('Password :')
                User(**auth).is_auth()
                self.account()
                return
        print(response)
        self.main()





    def main(self):
        try:
            menu = """
            1) login
            2) exit
            >>>"""
            key = input(menu)
            match key:
                case '1':
                    self.login_page()
                case '2':
                    return
        except AuthException as e:
            print(e)
            self.main()


