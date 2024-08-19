import random
from pathlib import Path
import smtplib, ssl
from module_3.lesson_4.ToDo.config.log_config import user_logger
from module_3.lesson_4.ToDo.errors.main import ErrorMessage
import bcrypt

BASE_PATH = Path(__file__).parent.parent


def send_email_code(receiver_email) -> int:
    pass



class Hash:
    def __init__(self, password = None , hash_password = None):
        self.password = password
        self.hash_password = hash_password

    def hashpw(self):
        pass

    def checkpw(self):
        pass






