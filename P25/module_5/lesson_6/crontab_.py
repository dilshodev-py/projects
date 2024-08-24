

users = [6694626582, 7327382994, 7033073770, 669138852, 5754977794, 1301667438, 6101028450, 5585005492]

import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = "7478312427:AAEkiYYGSIp-KvvEtSP3nUj04K1s2EH-dx0"


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    for i in users:
        await bot.send_message(chat_id=i , text="Hello")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())