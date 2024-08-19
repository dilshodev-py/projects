# requests package
import requests
import httpx

# HTTP protocol
"""
GET      response malumotni olish
POST     register
PUTCH    product(a , b)
PUT      product(a , b)
DELETE   product(id)
"""

# l = """https://telegra.ph/file/dbaa972d99037df30deed.png
# https://telegra.ph/file/4c60f0f213a795c75f8de.png
# https://telegra.ph/file/3f4acac79ad89f50d6f03.png
# https://telegra.ph/file/3e9c36e6559b032acf3a1.png
# https://telegra.ph/file/8af68a32da1df68422379.png
# """.split('\n')
# i  =0
# for url in l:
#     photo_response = requests.get(url)
#     with open(f"/home/dilshod/PycharmProjects/Python20/module_3/lesson_6/photo{i}.png", 'wb') as f:
#         f.write(photo_response.content)
#     i += 1


# print(photo_response.status_code)
# print(photo_response.content)
# print(photo_response.headers)
# print(photo_response.json())
# print(photo_response.url)
# print(photo_response.cookies)
# print(photo_response.request)


# POST     register



# i = 0
# while i <= 10000:
#     data = {
#         "uname": f"dilshodev{i}@gmail.com",
#         "pw1": f"123456{i}",
#         "dosavecreate": "Create Account"
#     }
#     response = requests.post("https://codingbat.com/pref", data = data)
#     i += 1
# response = requests.get("https://www.gstatic.com/recaptcha/releases/Ya-Cd6PbRI5ktAHEhm9JuKEu/recaptcha__ru.js")
# print(response.status_code)


# user = {
#   "id": 1000000,
#   "username": "botir4rt5",
#   "firstName": "botirjonert",
#   "lastName": "qodirovrew",
#   "email": "botir@gmail.com",
#   "password": "1234ret",
#   "phone": "+998993456789",
#   "userStatus": 0
# }
#
# response = requests.post("https://petstore.swagger.io/v2/user", data=user)
# print(response.json())
data={"name": "Dilshod Absaitov", "email": "dilshod@gmail.com", "password": "12345678"}


res = requests.post("https://mockapi.io/api/users" , data=data)
print(res.json())


