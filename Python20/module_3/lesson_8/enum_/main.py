from enum import Enum

# class Season(Enum):
#     SPRING = 1
#     SUMMER = 2
#     AUTUMN = 3
#     WINTER = 4
#
# class ROLE(Enum):
#     Manager = "MANAGER"
#     Admin = "ADMIN"
#     SuperAdmin = "SUPERADMIN"
#     User = "USER"

# print(ROLE["Manager"].value)

# print(Season.SUMMER.value)
# print(Season["SUMMER"].value)
#
#
# print(Season.SUMMER.name)
# print(Season(2).name)
#
#
# for season in Season:
#     print(season.value , "-" , season.name)
#
# def choose_season():
#     for i in Season:
#         print(f"{i.value}) {i.name}")
#     print(">>>")
#     key = int(input())
#     season = Season(key).name
# match key:
#     case 1:
#         season = "SPRING"
#     case 2:
#         season = "AUTUMN"
#     case 3:
#         season = "SUMER"
#     case 4:
#         season  = "WINTER"
# choose_season()


class A(Enum):
    Not_Found = 404