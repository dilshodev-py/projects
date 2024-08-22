import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from dispatcher import TOKEN
from bot.handlers import *

i18n = I18n(path="locales", default_locale="en")
async def register_all_middlewares():
    dp.update.middleware(FSMI18nMiddleware(i18n))
async def main() -> None:
    await register_all_middlewares()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


# ==================================================

# WEB_SERVER_HOST = "127.0.0.1"
# WEB_SERVER_PORT = 8080
# WEBHOOK_PATH = "/webhook"
# WEBHOOK_SECRET = "my-secret"
# BASE_WEBHOOK_URL = "https://9e88-178-218-201-17.ngrok-free.app"
#
# i18n = I18n(path="locales", default_locale="en")
#
#
# async def register_all_middlewares():
#     dp.update.middleware(FSMI18nMiddleware(i18n))
#
# async def on_startup(bot: Bot) -> None:
#     await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)
#
# def main() -> None:
#
#     asyncio.run(register_all_middlewares())
#     dp.startup.register(on_startup)
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     app = web.Application()
#
#     webhook_requests_handler = SimpleRequestHandler(
#         dispatcher=dp,
#         bot=bot,
#         secret_token=WEBHOOK_SECRET,
#     )
#     webhook_requests_handler.register(app, path=WEBHOOK_PATH)
#     setup_application(app, dp, bot=bot)
#     web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     main()