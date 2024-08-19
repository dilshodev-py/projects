"""
{
        "id" : "num",
        "card_number" : "1234123412341234",
        "term" : "12/24",
        "password" : 1111,
        "user_id" : 1
}
"""
import fileinput
import os

cards: list['Card'] = []

"""
{
        "id" : 1,
        "fullname" : "Botirjon",
        "username" : "botir434",
        "password" : "botir01"
}
"""
users: list['User'] = []


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        file = open(self.file_name, "r")
        datas = file.read().split("\n")
        file.close()
        return datas

    def write(self, data):
        file = open(self.file_name, "w")
        file.write(data)
        file.close()


file = File("/home/dilshod/PycharmProjects/Python20/module2/lesson_6/satr.txt")

data = file.read()

file.write('\n'.join(data))

"""
{
        "id" : "num",
        "from_card" : "1234123412341234",
        "to_card" : "4321432143214321",
        "summa" : 100_000,
        "datetime" : "2023-12-09 11:26:56.009876"
}
"""
histories: list['History'] = []


class CRUD:
    def save(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_val):
        pass


class User(CRUD):
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 username: str = None,
                 password: str = None):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def is_username(self):
        for user in users:
            if user.username == self.username:
                return True
        return False

    def is_valid(self):
        if self.is_username():
            raise Exception("Bunday username mavjud !")

        if len(self.username) < 5:
            raise Exception('Username 5 ta belgidan kam')
        if len(self.password) < 4:
            raise Exception('Password 4 ta belgidan kam')

    def is_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return user
        else:
            raise Exception("Bunday account mavjud emas !")

    def save(self):
        users.append(self)

    def get(self):
        for user in users:
            if user.id == self.id:
                return user

    def delete(self):
        for user in users:
            if user.id == self.id:
                users.remove(user)

    def update(self, field, new_val):
        user = self.get()
        if field == "fullname":
            user.fullname = new_val
        elif field == "username":
            user.username = new_val
        elif field == 'password':
            user.password = new_val


class Card(CRUD):
    def __init__(self,
                 id: int = None,
                 card_number: str = None,
                 term: str = None,
                 password: int = None,
                 balance: float = None,
                 user_id: int = None
                 ):
        self.id = id
        self.card_number = card_number
        self.term = term
        self.password = password
        self.balance = balance
        self.user_id = user_id

    def transaction(self, from_card, to_card, summ):  # TODO
        pass

    def is_valid(self):  # TODO
        if len(self.card_number) != 16:
            raise Exception("Card number invalid !")

    def sequence_id(self):
        return cards[-1].id + 1 if cards else 1

    def save(self):
        cards.append(self)

    def get(self):
        for card in cards:
            if card.id == self.id:
                return card

    def delete(self):
        for card in cards:
            if card.id == self.id:
                cards.remove(card)

    def update(self, field, new_val):
        for card in cards:
            if card.id == self.id:
                if field == "password":
                    card.password = new_val


users.append(User(1, "Bahrom Qodirov", "bahrom", "1111"))

session_user: User | None = None
"""
    1) Card
        1) card view
        2) card add
        3) card balance
        4) card transaction
        5) card delete  
        6) card change
    2) settings
        1) info
        2) change
            1) fullname
            2) username
            3) password
            >>>1
            new_val : 
        3) <-back
    3) logout
"""


class UI:

    def register(self):
        try:
            user = {
                "id": User().sequence_id(),
                "fullname": input("Fullname : "),
                "username": input("Username: "),
                "password": input("Password : ")
            }
            user = User(**user)
            user.is_valid()
            user.save()
            print("Mofaqiyatli account yaratildi !")
            print("_____________________________________")
            self.main()
        except Exception as e:
            print(e)
            self.main()

    def main(self):
        menu = """
        1) Register
        2) Login
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

    def account_menu(self):

        menu = """
            1) card
            2) settings
            3) logout
            >>>"""

        match input(menu):
            case "1":
                self.card_menu()
            case "2":
                self.profile()
            case "3":
                self.main()

    def card_menu(self):
        try:
            card_menu = """
                1) card add
                2) card view
                3) card balance       
                4) card transaction
                5) card delete  
                6) card change
                0) <- back
                >>>"""
            match input(card_menu):
                case "0":
                    self.account_menu()
                    return
                case "1":

                    card = {
                        "id": Card().sequence_id(),
                        "card_number": int(input("card number: ")),
                        "term": input("term[mm/YY] : "),
                        "balance": float(input("Balance : ")),
                        "password": int(input("password[1234] : ")),
                        "confirm_password": int(input("confirm password : ")),
                        "user_id": session_user.id
                    }
                    while card.get("password") != card.get("confirm_password"):
                        print("Password is wrong !")
                        card["password"] = int(input("password[1234] : "))
                        card["confirm_password"] = int(input("confirm password : "))
                    del card["confirm_password"]
                    card = Card(**card)
                    card.is_valid()
                    card.save()
                    self.card_menu()

                case "2":
                    for card in cards:
                        if card.user_id == session_user.id:
                            print(card.__dict__)

                    self.card_menu()
                    return

                case "3":
                    for i, card in enumerate(cards, 1):
                        if card.user_id == session_user.id:
                            print(f"{i}) {card.card_number}")
                    choose_index = int(input(">>>")) - 1
                    print(cards[choose_index].balance)
                    self.card_menu()
        except Exception as e:
            print(e)
            self.card_menu()


    def profile(self):

        menu = """
            1) info
            2) change
            0) <-back
        """
        match input(menu):
            case "1":
                print(session_user.__dict__)
                self.profile()
            case "2":

                field = """
                1) fullname
                2) username
                3) password
                0) <- back
                """
                key = input(field)
                if key == "0":
                    self.profile()
                    return
                new_val = input("new value : ")
                match key:
                    case "1":
                        session_user.fullname = new_val
                    case "2":
                        session_user.username = new_val
                    case "3":
                        session_user.password = new_val
                self.profile()
            case "0":
                self.account_menu()

    def login(self):
        try:
            global session_user
            auth = {
                "username": input("Username : "),
                "password": input("Password: ")
            }
            user = User(**auth)
            session_user = user.is_login()

        except Exception as e:
            print(e)
            self.main()


UI().main()
