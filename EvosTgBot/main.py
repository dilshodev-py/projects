import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.utils.i18n import FSMI18nMiddleware
from bot.handlers import *

from bot.dispatcher import dp, TOKEN, i18n, router


async def main() -> None:
    bot = Bot(TOKEN)
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

