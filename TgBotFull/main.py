import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import InlineQueryResultArticle, InlineQuery, InputTextMessageContent, Message

TOKEN = "6385276113:AAFTkoPVDR3xsV6tQ8PF-4n0h_s20RI6KWI"

# redis = Redis()
# storage = RedisStorage(redis)
dp = Dispatcher()
#
# BASE_DIR = Path(__file__).parent
# LOCALES_DIR = BASE_DIR / 'locales'
#
# i18n = I18n(path=LOCALES_DIR,)
#
# class UserState(StatesGroup):
#     firstname = State()
#     lastname = State()
d = [
    {
        "id": 1,
        "name": "Ikki dunyo",
        "image": "https://telegra.ph/file/a7d72d0c776605249fe51.png",
        "author": "Botirjon",
        "price": 150000,
    },
    {
        "id": 2,
        "name": "Oq kema",
        "image": "https://telegra.ph/file/d438ec818cb3dcd460243.png",
        "price": 100000,
        "author": "Botirjon",

    },
    {
        "id": 3,
        "name": "Pycharm Book",
        "image": "https://telegra.ph/file/feab6d06b25dc6231e686.png",
        "price": 1000000,
        "author": "Botirjon",

    },
    {
        "id": 4,
        "name": "Docker",
        "image": "https://telegra.ph/file/48a817e55b67756572ed0.png",
        "price": 1200000,
        "author": "Botirjon",

    }
]

text = """
    
"""

@dp.inline_query()
async def command_start_handler(inline_query: InlineQuery):
    result = [InlineQueryResultArticle(
            id=str(book.get("id")),
            title=str(book.get("title")),
            thumbnail_url=str(book.get("photo")),
            description=f"{book['author']}\nNarxi: {book['price']} {book['money_type']}",
            input_message_content=InputTextMessageContent(message_text=book.get("name"))) for book in d]
    await inline_query.answer(result, cache_time=5, is_personal=True)


#
#
@dp.message()
async def lang_handler(message: Message) -> None:
    print(message)
    # text = _("CHoose : ")
    # rkm = ReplyKeyboardBuilder()
    # rkm.add(*[
    #     KeyboardButton(text = "english"),
    #     KeyboardButton(text = "uzbek"),
    # ])
    await message.answer("salom")
#
#
# @dp.message(F.text == "register")
# async def eng_handler(message: Message, state: FSMContext):
#     text = _("First name : ")
#     await state.set_state(UserState.firstname)
#     await message.answer(text)
#
# @dp.message(UserState.firstname)
# async def eng_handler(message: Message, state: FSMContext):
#     text = _("Last name : ")
#     await state.update_data({"firstname" : message.text})
#     await state.set_state(UserState.lastname)
#     await message.answer(text)
#
# @dp.message(UserState.lastname)
# async def eng_handler(message: Message, state: FSMContext):
#     await state.update_data({"lastname" : message.text})
#     data = await state.get_data()
#     await state.clear()
#     await message.answer(f"{data}")
#
#
#
#
# @dp.message(F.text == "english")
# async def eng_handler(message: Message, state : FSMContext):
#     await state.update_data(data={"locale" : 'en'})
#     await message.answer(_("Change to English lang"))
#
# @dp.message(F.text == "uzbek")
# async def uz_handler(message: Message, state : FSMContext):
#     await state.update_data(data={"locale" : 'uz'})
#     await message.answer(_("Change to Uzbek lang"))
#
# @dp.message(F.text == __("salom"))
# async def my_handler(message: Message) -> None:
#     await message.answer(
#         _("Hello, {name}!").format(
#             name=html.quote(message.from_user.full_name)
#         )
#     )


async def main() -> None:
    bot = Bot(TOKEN)
    # dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# ===============================================================================

#
# import logging
# import sys
# from os import getenv
#
# from aiohttp import web
#
# from aiogram import Bot, Dispatcher, Router, types
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from aiogram.utils.markdown import hbold
# from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
# # sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
#
# TOKEN = "7149796467:AAEiHpUDQYQTc64ONrzOloAp4KWOMbZECJQ"
#
# WEB_SERVER_HOST = "127.0.0.1"
# WEB_SERVER_PORT = 8080
#
# WEBHOOK_PATH = "/webhook"
# WEBHOOK_SECRET = "my-secret"
# BASE_WEBHOOK_URL = "https://08f6-178-218-201-17.ngrok-free.app"
#
# router = Router()
#
#
# @router.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode=ParseMode.HTML)
#
#
# @router.message()
# async def echo_handler(message: types.Message) -> None:
#
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")
#
#
# async def on_startup(bot: Bot) -> None:
#     await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)
#
#
# def main() -> None:
#     dp = Dispatcher()
#     dp.include_router(router)
#
#     dp.startup.register(on_startup)
#
#     bot = Bot(TOKEN)
#
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
