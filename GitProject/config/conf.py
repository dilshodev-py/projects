import os
from pathlib import Path

from dotenv import load_dotenv
BASE_PATH = Path(__file__).parent.parent
load_dotenv(f"{BASE_PATH}/.env")


class DBConfig:
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")


class BotConfig:
    BOT_TOKEN = os.getenv("BOT_TOKEN")


class Conf:
    db = DBConfig()
    bot = BotConfig()



