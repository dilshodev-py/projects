from os import getenv
from dotenv import load_dotenv
from aiogram import Dispatcher
load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()