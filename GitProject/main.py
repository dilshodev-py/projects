import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from bot.handlers import *
from config.conf import Conf
from bot.dispatcher import dp

i18n = I18n(path="locales")


async def main() -> None:
    BOT_TOKEN = Conf.bot.BOT_TOKEN
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
