from os import getenv

from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis import Redis

from utils.conf import Config as conf

TOKEN = conf.bot.BOT_TOKEN
redis = Redis(host='redis')
dp = Dispatcher(storage=RedisStorage(redis))