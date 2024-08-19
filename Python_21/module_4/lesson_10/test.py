# crontab - time control

# * - har
# backup.tar
# 00:00 - > 0 0 * * *
# %Y:%m:%d %H:%M:%S.tar

# pdp food
# bot :
#     8:30 menu yaratildi zakas bering
#     9:00 menu yaratildi zakas bering
#     9:30 menu yaratildi zakas bering
#     10:00 menu yaratildi zakas bering

# 0 8,9,10 * * *
# 0 8-10 * * *

# 30 8 * * *
# */30 9-10 * * *

#
# with open("/home/dilshod/PycharmProjects/Python_21/module_4/lesson_10/hello.txt" , 'a') as f:
#     f.write('\nhello world')

import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.types import Message

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def command_start_handler(bot) -> None:
    await bot.send_message(id , f"Hello")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await command_start_handler(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())