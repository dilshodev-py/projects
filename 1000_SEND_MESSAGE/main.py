import asyncio
import logging
import sys
import time

import httpx
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7169306709:AAE9Vydeu8VHBJxFsz3QG9Uq2eGLtOcjucE"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    start = time.time()
    count = 0
    tasks = []
    while count < 50:
        if len(tasks) > 20:
            await asyncio.gather(*tasks)
            await asyncio.sleep(2)
            tasks = []
        tasks.append(bot.send_message(message.from_user.id, 'msg'))

    print(int(time.time() - start), f' s \nsoni - {count}')



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


'''
25
10s - 250
40s - 1000

11s - 50
22s - 100
220s - 1000

220,000s - 1,000,000
86400s ~ 3kun

'''