from dataclasses import dataclass

from db.servise import DbService
from utils import random_code

@dataclass
class User(DbService):
    id: int = None
    phone_number: str = None
    first_name: str = None
    last_name: str = None
    username: str = None
    photo: str = None
    is_premium: bool = False
    bio: str = None

    def sequence_id(self):
        users = self.objects()
        return int(users[-1].id) + 1 if users else 1

    def is_valid(self):
        users = self.objects()
        for user in users:
            if user.phone_number == self.phone_number:
                return False , "Already phone number !"
            elif user.username == self.username:
                return False , "Already username !"
        return True , 'Success'

    def save(self):
        users = self.objects()
        users.append(self)
        self.write(users)

    def send_code(self):
        code = str(random_code())
        with open('/home/dilshod/PycharmProjects/TgClone_hw/code.txt', 'w') as f:
            f.write(code)
        return code

    def is_login(self):
        users = self.objects()
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.send_code()
                f_code = input("code >>>")
                if code == f_code:
                    return True , user
                else:
                    return False , "invalid code!"

        return False , 'Not Found phone number !'