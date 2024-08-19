# # cards: list['Card'] = []
# #
# # class Card:
# #     def __init__(self,
# #                  id: int ,
# #                  card_number: int,
# #                  cvs : int,
# #                  balance : float,
# #                  password : int,
# #                  term : str, # '12/25'
# #                  join_date : str
# #                  ):
# #         self.id = id
# #         self.card_number = card_number
# #         self.cvs = cvs
# #         self.balance = balance
# #         self.password = password
# #         self.term = term
# #         self.join_date = join_date
# #
# #     def transfer(self, card_number: int ,amount: float):
# #         if amount > self.balance:
# #             return "Mablag' yetarli emas !"
# #
# #         for card in cards:
# #             if card_number == card.card_number:
# #                 card.balance += amount
# #                 self.balance -= amount
# #                 break
# #         else:
# #             return "Not found card !"
# #         return "Success !"
# #
# #
# # card1 = Card(1 , 1234123412341234 , 123 , 100_000 , 1111 , '12/25' , '2024-02-16')
# # card2 = Card(1 , 1234123412341235 , 124 , 0 , 0000 , '12/26' , '2024-02-16')
# # cards.append(card1)
# # cards.append(card2)
# #
# # print(card1.balance)
# # print(card1.transfer(1234123412341235, 60_000))
# # print(card1.balance)
# # print(card2.balance)
# # print(card2.transfer(1234123412341234, 30_000))
# # print(card2.balance)
# # print(card1.balance)
# # print(cards[1].balance)
# #
#
#
# """
# OOP tamoillari
#     class
#     object
#     inheritance (vorislik)
#     encapsulation
#     polymorphism
#     abstraction
#
# """
#
#
# class Animal:
#     def __init__(self, name, gender, habitat):
#         self.name = name
#         self.gender = gender
#         self.habitat = habitat
#
#     def print_info(self):
#         print(self.name, self.gender, self.habitat)
#
#
# class Bird:
#     def __init__(self, name, gender, habitat , is_fly : bool):
#         super().__init__(name, gender, habitat)
#         self.is_fly = is_fly
#
#     def print_info(self):
#         print(self.name, self.gender, self.habitat, self.is_fly)
#
#
#
# class Fish(Bird , Animal):
#     def __init__(self, name, gender, habitat):
#         super().__init__(name, gender, habitat)
#
#
# class Mammal(Animal):
#     def __init__(self, name, gender, habitat):
#         super().__init__(name, gender, habitat)

a = 10

def function():
    a = 20

function()
print(a)