from main import Users , Card , History
session_user : Users | None = None



class CardUI:
    def add(self):
        card = {
            "id": str(Card().sequence_id()),
            "card_number": input("Card number : "),
            'term': input("Term [month/year] : "),
            "password": input("Password : "),
            "confirm_password": input("Confirm password : "),
            "balance": input("Balance : "),
            "user_id" : session_user.id
        }
        i = 0
        while i <= 3 and card.get('password') != card.get("confirm_password"):
            card['password'] = input("Password : ")
            card['confirm_password'] = input("Confirm password : ")
            i += 1
        if i == 3:
            print("Urunishlar tugadi !")
            UI().card_menu()
            return
        del card['confirm_password']
        card = Card(**card)
        response = card.is_valid()
        if response:
            print(response)
            UI().card_menu()
            return
        card.save()
        print("Mofaqiyatli card qo'shildi !")
        UI().card_menu()

    def view(self):
        card = Card(user_id=session_user.id)
        cards = card.get_user_id()
        for card in cards:
            print(card)
        UI().card_menu()

    def transaction(self):
        card = Card(user_id=session_user.id)
        cards = card.get_user_id()
        for card in cards:
            print(f"{card[0]}) {card[1]}")
        card_id = input(">>>")
        to_card = input("To card number : ")
        summ = float(input("Summ : "))
        response = Card(id = card_id).transfer(to_card , summ)
        if response:
            print(response)
            UI().card_menu()
        print("Mofaqaiyatli pul o'tkazildi")
        UI().card_menu()

    def delete(self):
        card = Card(user_id=session_user.id)
        cards = card.get_user_id()
        for  card in cards:
            print(f"{card[0]}) {card[1]}")
        card_id = input(">>>")
        Card(id = card_id).delete()


    def change_password(self):
        card = Card(user_id=session_user.id)
        cards = card.get_user_id()
        for card in cards:

            print(f"{card[0]}) {card[1]}")
        card_id = input(">>>")


        choose = input("Password change [Yes/no] : ")

        if choose == 'no':
            UI().card_menu()
        new_password = input("New password : ")
        Card(id = card_id).change(new_password)
        UI().card_menu()





class UI:
    def register(self):
        user = {
            "id" : str(Users().sequence_id()),
            "fullname" : input("Fullname : "),
            "username" : input("Username : "),
            "password" : input("Password : ")
        }
        user = Users(**user)
        response = user.is_valid()
        if response:
            print(response)
            self.authentication()
            return
        user.save()
        print("============= Mofaqiyatli account yaratildi ! ==================")
        self.authentication()

    def login(self):
        global session_user
        auth = {
            "username" : input("Username : "),
            "password" : input("Password : ")
        }
        user = Users(**auth)
        user = user.is_login()
        if user:
            session_user = user
            print('Welcome account')
            self.account_menu()
            return
        print("Bunday account mavjud emas !")
        self.authentication()

    def authentication(self):
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

    def account_menu(self):
        global session_user
        menu = """
        1) cards
        2) settings
        3) logout
        >>>"""
        match input(menu):
            case "1":
                self.card_menu()
            case "2":
                self.user_settings()
            case "3":
                session_user = None
                self.authentication()
    def card_menu(self):
        menu = """
        CARD MENU
        1) Add
        2) View
        3) Transaction
        4) Change
        5) Delete
        0) <- back
        >>>"""
        match input(menu):
            case '0':
                self.account_menu()
            case '1':
                CardUI().add()
            case "2":
                CardUI().view()
            case "3":
                CardUI().transaction()
            case "4":
                CardUI().change_password()
            case "5":
                CardUI().delete()
            case "6":
                self.account_menu()

    def user_settings(self):
        pass


UI().authentication()

