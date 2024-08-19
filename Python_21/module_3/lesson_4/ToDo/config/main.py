import random
from pathlib import Path
import smtplib, ssl
from module_3.lesson_4.ToDo.config.log_config import user_logger
from module_3.lesson_4.ToDo.errors.main import ErrorMessage
import bcrypt

BASE_PATH = Path(__file__).parent.parent


async def send_email_code(receiver_email) -> int:
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "absaitovdev@gmail.com"  # Enter your address
    password = "hatechvvjiywdmhm"
    code = random.randrange(100_000 , 1_000_000)
    message = f"""
    Code : {code}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return code



class Hash:
    def __init__(self, password = None , hash_password = None):
        self.password = password
        self.hash_password = hash_password

    async def hashpw(self):
        salt = bcrypt.gensalt()
        hash_p = bcrypt.hashpw(self.password.encode() , salt)

        return hash_p.decode()

    async def checkpw(self):
        return bcrypt.checkpw(self.password.encode(), self.hash_password.encode())







