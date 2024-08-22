import asyncio
import logging
import os
import sys
import time

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, Update
from dotenv import load_dotenv
from itertools import cycle
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()

users = [6694626582, 7327382994, 7033073770, 669138852, 5754977794, 1301667438, 6101028450, 5585005492]


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Salom {message.from_user.first_name}")


@dp.message(Command('send'))
async def send(message: Message):
    tasks = []
    start = time.time()
    count = 0
    for i in cycle(users):
        if count == 100:
            break
        if len(tasks) == 28:
            await asyncio.gather(*tasks)
            tasks = []
        tasks.append(message.bot.send_message(i , text = "salom"))
        count += 1
    end = time.time()
    await message.answer(text = f"Time: {end-start}")


    # start = time.time()
    # for user in users:
    #     await message.bot.send_message(user, f"Hello {message.text}!")

#     stop = time.time()
#     duration = stop - start
#     await message.answer(text =  f'{duration}')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
