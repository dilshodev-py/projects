from os import getenv

from aiogram import Router, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n import I18n
from dotenv import load_dotenv
from redis.asyncio import Redis

load_dotenv('.env')

TOKEN = getenv("BOT_TOKEN")

router = Router()
i18n = I18n(path="locales")
redis = Redis()
dp = Dispatcher(storage=RedisStorage(redis))