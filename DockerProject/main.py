import asyncio
import logging
import os
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import psycopg2
from dotenv import load_dotenv
load_dotenv()

con = psycopg2.connect(
    dbname= os.getenv("DB_NAME"),
    user= os.getenv("DB_USER"),
    password= os.getenv("DB_PASSWORD"),
    host= os.getenv("DB_HOST"),
    port= os.getenv("DB_PORT")
)
cur = con.cursor()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    query = "insert into users(user_id , fullname) values (%s , %s)"
    params = (message.from_user.id , message.from_user.full_name)
    cur.execute(query,params)
    con.commit()
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")



@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
# docker image prune

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())