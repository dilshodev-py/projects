from pathlib import Path
from random import randrange
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from colorama import Fore

from apps.language.lang import data

BASE_URL = Path(__file__).parent.parent.parent


class Email:

    async def make_code(self):
        code = randrange(10 ** 5, 10 ** 6)
        return code

    async def send_email_code(self, receiver_email):
        code = await self.make_code()
        sender_email = "absaitovdev@gmail.com"
        password = "xdaogcqthhoidbug"
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        html = f"""
            <h1>Code : {code}</h1>
        """
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return code

class Sticker:
    user_stickers = ['🎅', '👩', '👮', '🕵', '🧕', '👸']

    async def user(self):
        for pos , sticker in enumerate(self.user_stickers,1):
            print(f"{pos}) {sticker}")
        pos = int(input(Fore.BLUE+">>>"))
        return self.user_stickers[pos-1]


class Lang:
    langs = list(data.keys())   # ['uz' , 'en']
    async def choose_lang(self):
        for pos , lang in enumerate(self.langs,1):
            print(f"{pos}) {lang}")
        pos = int(input(Fore.BLUE+">>>"))
        return self.langs[pos-1]







class Settings:
    email = Email()
    sticker = Sticker()
    lang = Lang()
