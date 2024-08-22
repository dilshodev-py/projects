from db.models import Product

# products = [
#     {
#         "name": "Coca cola",
#         "discount": 10,
#         "price": 12000,
#         "aksiya": True,
#         "description": "Zararli ichimlik",
#         "photo": "https://telegra.ph/file/2b26460bda98eb6eaebd0.png",
#         "category_id": 11,
#     },
#     {
#         "name": "Mol go'shtidan shaurma",
#         "discount": 0,
#         "price": 30000,
#         "aksiya": False,
#         "description": "Shirali gril mol go'shti, yangi bodring va shirali pomidor bo'lakchalari, kunjut "
#                        "urug'lari sepilgan yarim doira shaklli shirin iforga ega bulochkada "
#                        "yangi piyoz va ko'katli tomat sousi ostidagi qarsildoq kartoshka chipslari bilan",
#         "photo": "https://cp.ectn.uz/files//shaurma_govajiy_22_01.png",
#         "category_id": 12,
#     },
#     {
#         "name": "Fanta",
#         "discount": 20,
#         "price": 14000,
#         "aksiya": True,
#         "description": "Haddan tashqari shirin",
#         "photo": "https://telegra.ph/file/933fa0afd4c74fa9664e8.png",
#         "category_id": 11
#     },
#
#     {
#         "name": "Mountain Dew",
#         "discount": 10,
#         "price": 10000,
#         "aksiya": True,
#         "description": "O'zgacha ta'm",
#         "photo": "https://telegra.ph/file/8473c690e3c6461cdde2f.png",
#         "category_id": 11
#     },
#     {
#         "name": "Set",
#         "discount": 0,
#         "price": 89000,
#         "aksiya": 'false',
#         "description": "Double Set Series - ikki kishi uchun foydali yechim! 1-sonli qo'sh to'plamga mol go'shti va qarsillab kartoshkali smayliklar qo'shilgan pita nonining ikki porsiyasi va, albatta, 2 stakan Pepsi kiradi.",
#         "photo": "https://telegra.ph/file/d857388f279a4903f98e5.png",
#         "category_id": 16
#     },
#     {
#         "name": "Mini lavash",
#         "discount": 2,
#         "price": 27000,
#         "aksiya": True,
#         "description": "Yeyishga arzidi",
#         "photo": "",
#         "category_id": 11,
#     },
#     {
#         "name": "Cheese cake",
#         "discount": 5,
#         "price": 45000,
#         "aksiya": True,
#         "description": "Wonderful taste!",
#         "photo": "https://telegra.ph/file/613a67d40c9c735ec0fa5.png",
#         "category_id": 15,
#     },
#     {
#         "name": "Donar mol go'shtli",
#         "discount": 10,
#         "price": 45000,
#         "aksiya": True,
#         "description": """
#         Kombinatsiyali idishda shirali gril mol go'shti bo'lakchalari, tillarang kartoshka-fri, miks-guruch, tabiiy,
#         o'zimizda tayyorlangan salat,
#         maxsus sous va shirin iforga ega kulcha non
#         """,
#         "photo": "https://cp.ectn.uz/files//donar_govajiy_22_01.png",
#         "category_id": 12,
#     },
#     {
#         "name": "Tandir lavash",
#         "discount": 0,
#         "price": 36000,
#         "aksiya": True,
#         "description": "Onamiz yopgandek mazzali",
#         "photo": "https://telegra.ph/file/ba6f49b9dfd95f5c1db73.png",
#         "category_id": 14
#     },
#     {
#         "name": "Tovuq bilan trindvich",
#         "discount": 10,
#         "price": 25000,
#         "aksiya": True,
#         "description": "Grilda pishirilgan tovuq go'shti, yangi bodring va suvli pomidorning shirali bo'laklari.",
#         "photo": "https://telegra.ph/file/ebd569bee7da193b5c192.png",
#         "category_id": 14,
#     },
#     {
#         "name": "set1",
#         "discount": 7,
#         "price": 33000,
#         "aksiya": True,
#         "description": "pulingizni tejang!",
#         "photo": "https://telegra.ph/file/a2d996ee4ee78e548666e.png",
#         "category_id": 16,
#     },
#     {
#         "name": "Ice cream",
#         "discount": 0,
#         "price": 15000,
#         "aksiya": False,
#         "description": "Mazzali muzqaymoq",
#         "photo": "https://telegra.ph/file/c5fccf3bf1c7225362ff1.png",
#         "category_id": 15,
#     },
# ]
# for product in products:
#     Product(**product).insert()
