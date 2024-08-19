import json

file = open("cards.json", "r")
cards = json.load(file)
file.close()
session_card: None | dict = None
""" CARD 
{
    "id":1,
    "card_number":2826875762989573,
    "expire":"2024-03",
    "password":6175,
    "balance":81580.06
}
"""


class Card:
    def __init__(self,
                 id=None,
                 card_number=None,
                 expire=None,
                 password=None,
                 balance=None
                 ):
        self.id = id
        self.card_number = card_number
        self.expire = expire
        self.password = password
        self.balance = balance

    def is_valid(self):
        if not self.card_number.isdigit():
            return "Invalid card !"
        if len(str(self.password)) != 4:
            return "Invalid password"
        if int(self.expire.split("-")[0]) > 12:
            return "Expire invalid "
        self.card_number = int(self.card_number)

    def is_auth(self):
        for card in cards:
            if card.get("card_number") == self.card_number and card.get("expire") == self.expire and card.get(
                    "password") == self.password:
                return card

    def is_card(self, card_number):
        for card in cards:
            if card_number == card.get("card_number"):
                return card
        return False

    def transaction(self, to_card, summ: float):
        if summ >= self.balance:
            return False, "Dengi yetarli emas !"

        card: dict | bool = self.is_card(to_card)
        if not card:
            return False, "Bunday karta mavjud emas :("
        card["balance"] += summ
        from_card = self.is_card(self.card_number)
        from_card['balance'] -= summ
        return from_card , "Success transaction"

    def paynet(self, phone_number: str, summ: float):
        if summ >= self.balance:
            return False, "Paynet uchun Dengi yetarli emas !"

        from_card = self.is_card(self.card_number)
        from_card['balance'] -= summ
        return from_card , f"Success paynet to {phone_number}"


class CardUI:

    def card_menu(self):
        global session_card
        menu = """
            1) Transaction
            2) paynet
            3) balance
            4) settings
            0) logout
            >>>"""
        key = input(menu)
        match key:
            case "1":
                form = {
                    "to_card": int(input("To card : ")),
                    "summ": float(input("Summ [5000.0] : "))
                }

                is_card , message = Card(**session_card).transaction(**form)
                if is_card:
                    session_card = is_card
                print(message)
                self.card_menu()

            case "2":
                form = {
                    "phone_number": input("Phone number : "),
                    "summ": float(input("Summ [5000.0] : "))
                }
                is_paynet , message = Card(**session_card).paynet(**form)
                if is_paynet:
                    session_card = is_paynet
                print(message)
                self.card_menu()
            case "3":
                print("Your Balance : ",session_card.get("balance"))
                self.card_menu()
            case "0":
                UI().main()

    def auth(self):
        global session_card
        card = {
            "card_number": input("card_number : "),
            "expire": input("expire : "),
            "password": int(input("password : "))
        }
        card = Card(**card)
        isvalid = card.is_valid()
        if isvalid:
            print(isvalid)
            UI().main()
            return
        session_card = card.is_auth()
        if not session_card:
            print("Not found card !")
            UI().main()
            return
        self.card_menu()


class UI:

    def main(self):
        menu = """
            1) Enter card
            2) exit
            >>>"""
        key = input(menu)
        match key:
            case "1":
                CardUI().auth()
            case "2":
                return

UI().main()
