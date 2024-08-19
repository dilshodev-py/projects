from os import getenv
from dotenv import load_dotenv

load_dotenv('/home/dilshod/PycharmProjects/FactorBook23/.env')


class Bot:
    BOT_TOKEN = getenv('TOKEN')
    PAYMENT_CLICK_TOKEN = getenv("PAYMENT_CLICK_TOKEN")

class DB:
    DB_USER = getenv('DB_USER')
    DB_NAME = getenv('DB_NAME')
    DB_HOST = getenv('DB_HOST')
    DB_PORT = getenv('DB_PORT')
    DB_PASSWORD = getenv('DB_PASSWORD')

class Web:
    USERNAME = getenv('ADMIN_USERNAME')
    PASSWORD = getenv('ADMIN_PASSWD')
class Config:
    bot = Bot()
    db = DB()
    wb = Web()
