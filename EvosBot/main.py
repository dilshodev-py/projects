import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from dispatcher import TOKEN, dp
from bot.handlers import *

i18n = I18n(path="locales", default_locale="en")
async def register_all_middlewares():
    dp.update.middleware(FSMI18nMiddleware(i18n))
async def main() -> None:
    await register_all_middlewares()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())