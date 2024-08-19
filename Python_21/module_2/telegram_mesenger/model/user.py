from abc import ABC, abstractmethod
import random

from module_2.telegram_mesenger.error import ErrorMessage
from module_2.telegram_mesenger.model.tmp import UserDTO, AbstractCRUD


class User(UserDTO, AbstractCRUD):

    def is_valid(self):
        self.username_valid()
        self.phone_number_valid()

    def phone_number_valid(self):
        if len(self.phone_number) != 13:
            raise ErrorMessage('invalid number!')
        users = self.user_list()
        for user in users:
            if user.phone_number == self.phone_number:
                raise ErrorMessage("Already registered phone number")

    def sequence_id(self):
        users: list[UserDTO] = self.user_list()
        return int(users[-1].id) + 1 if users else 1

    def send_code(self):
        code = str(random.randrange(100_000, 1_000_000))
        with open("/home/dilshod/PycharmProjects/Python_21/module_2/telegram_mesenger/phone_message.txt", "w") as f:
            f.write(code)
        return code

    def is_auth(self):
        users = self.user_list()
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.send_code()
                valid_code = input('Code: ')
                if code != valid_code:
                    raise ErrorMessage('invalid code')
                return user
        else:
            raise ErrorMessage('not found account') # login

    def save(self):
        users = self.user_list()
        users.append(self)
        UserDTO.write(users)

    def username_valid(self):
        users = self.user_list()
        for user in users:
            if user.username == self.username:
                raise ErrorMessage('already exists')

    def update(self, filed, new_val):
        users = self.user_list()
        for user in users:
            if user.id == self.id:
                if filed == 'username':
                    self.username = new_val
                    self.username_valid()
                    user.username = new_val
                elif filed == 'fullname':
                    user.fullname = new_val
                elif filed == 'bio':
                    user.bio = new_val
                elif filed == 'photo':
                    user.photo = new_val
                elif filed == 'phone_number':
                    code = self.send_code()
                    valid_code = input('Code: ')
                    if valid_code != code:
                        raise ErrorMessage('wrong code')
                    user.phone_number = new_val
                return user
            UserDTO.write(users)

    def delete(self):
        users = self.user_list()
        for user in users:
            if self.id == user.id:
                users.remove(user)
                break
        UserDTO.write(users)

    def user_list(self):
        users: list[UserDTO] = UserDTO.read()
        return users

    def get(self):
        users = self.user_list()
        for user in users:
            if user.id == self.id:
                return user

    def show_users(self):
        users = self.user_list()

        for user in users:
            if self.username.lower() in user.username.lower():
                print(f"{user.id}) {user.username}")
