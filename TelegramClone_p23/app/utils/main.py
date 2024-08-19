import random
from abc import ABC, abstractmethod


def send_code():
    code = str(random.randrange(100_000 , 1_000_000))
    with open("/home/dilshod/PycharmProjects/TelegramClone_p23/phone_number.txt", "w") as f:
        f.write(code)

    return code

class CrudAbstract(ABC):
    @abstractmethod
    def sequence_id(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self, field, new_val):
        pass

    @abstractmethod
    def get(self):
        pass

