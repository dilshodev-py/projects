# from itertools import groupby
# a = "hhelelllooo     John"
# [print(i[0], end='') for i in groupby(a)]

# result = a[0]
# for i in a[1:]:
#     if result[-1] != i:
#         result += i
# print(result)

# a = "hhellllooo John"
# result = ""
# for i in a:
#     if not i in result:
#         result += i
# print(result)

# helo Jn

# .txt
# open() -> x , a , w , r
# dict append -> dict_name.update([(key , value)]) , dict_name[key] = value
# num = int(input()) # 5
# file = open("tast.txt", 'w')
# result = ""
# for i in range(num):
#     result += (num-i-1)*"  " + "*\n"
# result = result.rstrip('\n')
# file.write(result)
# file.close()
# file = open('tast.txt' , 'r')
# for i in file.readlines():
#     print(i.strip('\n'))
# file.close()
import datetime


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self) -> list[str]:
        with open(self.file_path, 'r') as file:
            return file.read().split('\n') # ['']

    def write(self, data: str):
        file = open(self.file_path, 'w')
        file.write(data)
        file.close()


class Users:
    def __init__(self,
                 id=None,
                 fullname=None,
                 username=None,
                 password=None):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def save(self):
        user_str = ",".join(self.__dict__.values())
        file = File('users.txt')
        data = file.read()
        if data[0] == "":
            del data[0]
        data.append(user_str)
        file.write("\n".join(data))

    def get_id(self):
        file = File("users.txt")
        users = file.read()
        for i in users:
            if i.split(",")[0] == self.id:
                return i

    def delete(self):
        file = File("users.txt")
        users = file.read()
        for i in users:
            if i.split(",")[0] == self.id:
                users.remove(i)
        file.write("\n".join(users))

    def sequence_id(self):
        file = File("users.txt")
        return int(file.read()[-1].split(",")[0]) + 1 if file.read()[0] != ''  else 1

    def update(self, field, new_val):
        file = File("users.txt")
        users = file.read()
        for i, user in enumerate(users):
            user = user.split(',')
            if user[0] == self.id:
                if field == "fullname":
                    user[1] = new_val
                if field == "username":
                    user[2] = new_val
                if field == "password":
                    user[3] = new_val
                user = ",".join(user)
                users[i] = user
        file.write('\n'.join(users))

    def is_login(self):
        file = File('users.txt')
        users: list[str] = file.read()
        for user in users:
            user = user.split(',')  # ['1' , 'botir' , 'botir01' , '1111']
            if user[2] == self.username and user[3] == self.password:
                return Users(*user)

    def unique_username(self):
        file = File('users.txt')
        users: list[str] = file.read()
        for user in users:
            user = user.split(',')
            if users[0] != '' and user[2] == self.username:
                return True
        return False

    def is_valid(self):
        if self.unique_username():
            return "Bunday username oladin ishlatilgan"
        if len(self.password) < 4:
            return 'Password qisqa berilgan !'


class Card:
    def __init__(self,
                 id: str = None,
                 card_number: str = None,
                 term: str = None,
                 password: str = None,
                 balance: str = None,
                 user_id: int = None):
        self.id = id
        self.card_number = card_number
        self.term = term
        self.password = password
        self.balance = balance
        self.user_id = user_id

    def sequence_id(self):
        file = File("cards.txt")
        return int(file.read()[-1].split(",")[0]) + 1 if file.read()[0] != '' else 1


    def is_valid(self):
        if len(self.card_number) != 16:
            return "Card number invalid !"
        if int(self.term.split('/')[0]) > 12:
            return 'Term invalid !'
        if len(self.password) != 4:
            return 'Password invalid'
        if float(self.balance) < 0:
            return "Balance not can not be manfiy !"

    def save(self):
        card = ','.join(self.__dict__.values())
        file = File('cards.txt')
        cards: list[str] = file.read()
        if cards[0] =='':
            del cards[0]
        cards.append(card)
        file.write('\n'.join(cards))

    def get_user_id(self):
        file = File('cards.txt')
        cards: list[str] = file.read()
        result_cards = []
        for card in cards:
            card = card.split(',')
            if card[-1] == self.user_id:
                result_cards.append(card)
        return result_cards

    def get_id(self):
        file = File('cards.txt')
        cards: list[str] = file.read()
        for card in cards:
            card = card.split(',')
            if card[0] == self.id:
                return Card(*card)

    def change(self, new_val):
        file = File('cards.txt')
        cards: list[str] = file.read()
        for i, card in enumerate(cards):
            card = card.split(',')
            if card[0] == self.id:
                card[3] = new_val
                card = ','.join(card)
                cards[i] = card
                break
        file.write("\n".join(cards))

    def balance_add(self, summ):
        file = File('cards.txt')
        cards: list[str] = file.read()
        for i, card in enumerate(cards):
            card = card.split(',')
            if card[0] == self.id or card[1] == self.card_number:
                card[-2] = str(float(card[-2]) + float(summ))
                cards[i] = ','.join(card)
                break
        file.write('\n'.join(cards))


    def delete(self):
        file = File('cards.txt')
        cards: list[str] = file.read()
        for card in cards:
            if card.split(',')[0] == self.id:
                cards.remove(card)
                file.write('\n'.join(cards))
                return "Mofaqiyatli o'chirildi"

        return "Bunday card number mavjud emas !"

    def transfer(self, to_card: str, summ):
        file = File('cards.txt')
        cards: list[str] = file.read()
        is_from_card = False
        is_to_card = False
        for i, card in enumerate(cards):
            card = card.split(',')
            if self.id == card[0] and float(card[-2]) > summ:
                is_from_card = True
            elif self.id == card[0] and float(card[-2]) < summ:
                return "Hisobingizda mablag' yetarli emas !"

        for i, card in enumerate(cards):
            card = card.split(',')
            if to_card == card[1]:
                is_to_card = card
                break
        else:
            return "To card topilmadi "

        if is_from_card and is_to_card:
            self.balance_add(-summ)
            Card(card_number=to_card).balance_add(summ)




class History:
    def __init__(self,
                 id: str = None,
                 from_card: str = None,
                 to_card: str = None,
                 summ: str = None,
                 datetime: str = None):
        self.id = id
        self.from_card = from_card
        self.to_card = to_card
        self.summ = summ
        self.datetime = datetime

    def sequence_id(self):
        file = File("histories.txt")
        return int(file.read()[-1].split(",")[0]) + 1 if file.read()[0] != '' else 1

    def save(self):
        new_history = ','.join(self.__dict__.values())
        file = File('histories.txt')
        histories: list[str] = file.read()
        if histories[0] =='':
            del histories[0]
        histories.append(new_history)
        file.write('\n'.join(histories))


    def get_list(self):
        file = File('histories.txt')
        histories: list[str] = file.read()
        for history in histories:
            history = history.split(',')
            if history[1] == self.from_card:
                print(f"{self.from_card} -> {history[2]} | SUM : {history[3]}  | DATETIME : {history[-1]}")


    def clear(self):
        File('histories.txt').write('')


    def delete(self):
        file = File('histories.txt')
        histories: list[str] = file.read()
        for history in histories:
            if history.split(',')[1] == self.from_card:
                histories.remove(history)
        file.write('\n'.join(histories))



