# # from pydantic.v1 import BaseModel, validator
# #
# # users = [
# #     {
# #         'id': '1',
# #         'first_name': 'Botir',
# #         'last_name': "Kamolov",
# #         'username': 'botir1',
# #         'password': 1234,
# #     }
# # ]
# #
# #
# # class Color(BaseModel):
# #     id: int = None
# #     name: str = None
# #
# #
# # class User(BaseModel):
# #     id: int = None
# #     first_name: str = None
# #     last_name: str = None
# #     username: str = None
# #     password: str = None
# #     color: Color = None
# #
# #     @validator('username')
# #     @classmethod
# #     def validate_username(cls, value):
# #         for user in users:
# #             if user.get("username") == value:
# #                 raise Exception('Already exists username !')
# #         return value
# #
# #     @validator('password')
# #     @classmethod
# #     def validate_password(cls, value):
# #         if len(value) < 4:
# #             raise Exception('invalid password !')
# #         return value
# #
# #
# # u = User(id='1',
# #          first_name='Botir',
# #          last_name="Kamolov",
# #          username='botir',
# #          password=1234,
# #          color=Color(id=10, name='black'))
# #
# # print(u.password)
# from datetime import datetime
#
# from pydantic.v1 import BaseModel, validator
# from string import punctuation
#
#
# class User(BaseModel):
#     id: int = None
#     fullname: str = None
#     phone_number: str = None
#     password: str = None
#     join_at: str = None
#
#     @validator('fullname')
#     @classmethod
#     def validate_fullname(cls, value):
#         if len(value.split()) <= 1:
#             raise Exception("Invalid Fullname !")
#         return value
#
#     @validator('phone_number')
#     @classmethod
#     def validate_phone_number(cls, value):
#         if not value.startswith('+'):
#             value = "+" + value
#         if (not value.startswith('+998')) or not value[1:].isdigit():
#             raise Exception("Phone number invalid")
#         return value
#
#     @validator('password')
#     @classmethod
#     def validator_password(cls, value):
#         is_valid = {
#             "number": False,
#             "lower": False,
#             "upper": False,
#             "punctuation": False
#         }
#         if len((value)) >= 4:
#             for i in value:
#                 if i.isdigit():
#                     is_valid['number'] = True
#                 elif i.islower():
#                     is_valid['lower'] = True
#                 elif i.isupper():
#                     is_valid['upper'] = True
#                 elif i in punctuation:
#                     is_valid['punctuation'] = True
#             if sum(is_valid.values()) != 4:
#                 raise Exception("Password invalid !")
#         else:
#             raise Exception("Password invalid !")
#         return value
#
#     @validator('join_at')
#     @classmethod
#     def validate_join_at(cls, value):
#         try:
#             datetime.fromisoformat(value)
#         except:
#             raise Exception("invalid join_at !")
#         return value
#
#
# user = {
#     "id": 1,
#     "fullname": "botir qodirov",
#     "phone_number": "+998993583231",
#     "password": '1T,r',
#     "join_at": str(datetime.now())
# }
#
# u = User(**user)
# print(u.phone_number)


