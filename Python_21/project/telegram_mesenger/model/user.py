from abc import ABC, abstractmethod
import random

from module_2.telegram_mesenger.error import ErrorMessage
from module_2.telegram_mesenger.model.tmp import UserDTO


class AbstractCRUD(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self, filed, new_val):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get(self):
        pass


class User(UserDTO, AbstractCRUD):

    def is_valid(self):
        if len(self.phone_number) != 13:
            raise ErrorMessage("Invalid phone number !")
        self.username_valid()


    def sequence_id(self):
        users: list[UserDTO] = self.user_list()
        return int(users[-1].id) + 1 if users else 1

    def send_code(self):
        code = str(random.randrange(100_000 , 1_000_000))
        with open("/home/dilshod/PycharmProjects/Python_21/module_2/telegram_mesenger/phone_message.txt", "w") as f:
            f.write(code)
        return code

    def is_auth(self):
        users : list[UserDTO] = self.user_list()
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.send_code()
                valid_code = input("Code : ")
                if code != valid_code:
                    raise ErrorMessage("Wrong code !")
                return user
        else:
            raise ErrorMessage("Not Found account !")



    def save(self):
        users: list[UserDTO] = self.user_list()
        users.append(self)
        UserDTO.write(users)

    def username_valid(self):
        users: list[UserDTO] = self.user_list()
        for user in users:
            if user.username == self.username:
                raise ErrorMessage("Already exists username !")


    def update(self, filed, new_val):
        users : list[UserDTO] = self.user_list()
        for user in users:
            if user.id == self.id:
                if filed == "username":
                    self.username = new_val
                    self.username_valid()
                    user.username = new_val
                elif filed == "fullname":
                    user.fullname = new_val
                elif filed == "bio":
                    user.bio = new_val
                elif filed == "photo":
                    user.photo = new_val
                elif filed == "phone_number":
                    code = self.send_code()
                    valid_code = input("Code : ")
                    if code != valid_code:
                        raise ErrorMessage("Wrong code !")
                    user.phone_number = new_val
        UserDTO.write(users)

    def delete(self):
        users : list[UserDTO] = self.user_list()
        for user in users:
            if user.id == self.id:
                users.remove(user)
                break
        UserDTO.write(users)

    def user_list(self):
        users : list[UserDTO] = UserDTO.read()
        return users

    def get(self):
        users : list[UserDTO] = self.user_list()
        for user in users:
            if user.id == self.id:
                return user
