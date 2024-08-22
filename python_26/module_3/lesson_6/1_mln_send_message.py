import asyncio
import logging
import sys
from os import getenv
from time import time

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from itertools import cycle



TOKEN = ''

dp = Dispatcher()
users = [1300817834 ,
         5647453083 ,
         6635413428 ,
         882090673 ,
         860359200,
         6203274805,
         7398145504,
         917620128,
         912893882,
         7169282667,
         7203022689,
         7327382994,
         7033073770,
         1148477816]

@dp.message(CommandStart() , F.from_user.id == 1148477816)
async def command_start_handler(message: Message):
    start = time()
    count = 0
    tasks = []
    i = iter(cycle(users))
    while True:
        if len(tasks) > 14:
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.5)
            tasks = []

        count += 1
        if count == 1000:
            break
        tasks.append(message.bot.send_message(next(i), 'msg'))

    print(int(time() - start), f' s \nsoni - {count}')



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())