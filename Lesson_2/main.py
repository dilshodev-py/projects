import asyncio
import datetime
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, F
from aiogram import html
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, I18n, I18nMiddleware, FSMI18nMiddleware
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv
from redis.asyncio import Redis

load_dotenv('.env')
# database connection telegram bot

TOKEN = getenv("BOT_TOKEN")

router = Router()
i18n = I18n(path="locales")


@router.message(Command("lang"))
async def lang_handler(message: Message):
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[
        KeyboardButton(text=_("Uzbek 🇺🇿")),
        KeyboardButton(text=_("Enlish 🇬🇧"))
    ])
    await message.answer(_("Choose language"), reply_markup=rkm.as_markup(resize_keyboard=True))


@router.message(F.text == __("Uzbek 🇺🇿"))
async def uzb_handler(message: Message, state: FSMContext):
    await state.update_data({"locale": "uz"})
    await message.answer(_("Change language to uz"))


@router.message(F.text == __("Enlish 🇬🇧"))
async def en_handler(message: Message, state: FSMContext):
    await state.update_data({"locale": "en"})
    await message.answer(_("Change language to en"))


@router.message(CommandStart())
async def my_handler(message: Message) -> None:
    await message.answer(_(f"Hello!") + f"{message.from_user.full_name}")


@router.message(F.text == __("today"))
async def today_handler(message: Message):
    text = _("Today") + f": {datetime.date.today()}"
    await message.answer(text)


# =========================================================================

# class UserState(StatesGroup):
#     first_name = State()
#     last_name = State()
#     age = State()
#
#
# @router.message(Command("register", prefix="/"))
# async def register(message: Message, state: FSMContext):
#     await state.set_state(UserState.first_name)
#     await message.answer("Ismingizni kiritng : ")
#
#
# @router.message(UserState.first_name)
# async def first_name_handler(message: Message, state: FSMContext):
#     await state.update_data({"first_name": message.text})
#     await state.set_state(UserState.last_name)
#     await message.answer("Familyangizni kiritng : ")
#
#
# @router.message(UserState.last_name)
# async def last_name_handler(message: Message, state: FSMContext):
#     await state.update_data({"last_name": message.text})
#     await state.set_state(UserState.age)
#     await message.answer("Yoshni kiritng : ")
#
#
# @router.message(UserState.age)
# async def age_handler(message: Message, state: FSMContext):
#     await state.update_data({"age": message.text})
#     data = await state.get_data()
#     await state.clear()
#     await message.answer(f"Sizning malumotlaringiz : {data}")


# def btn():
#     rkm = ReplyKeyboardBuilder()
#
#     rkm.add(*[
#         KeyboardButton(text = "Location", request_location=True),
#         KeyboardButton(text = "Contact", request_contact=True),
#         KeyboardButton(text = "Fullname")
#     ])
#     rkm.adjust(2, repeat=True)
#     return rkm.as_markup(resize_keyboard = True )
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode=ParseMode.HTML, reply_markup=btn())
#
# @dp.message((F.text == "salom") | (F.text == "hello"))
# async def salom_handler(message :Message):
#     await message.answer("Salom")
#
# @dp.message(F.text == "Fullname")
# async def fullname_handler(message: Message):
#     await message.answer(message.from_user.full_name)


# pybabel init -i locales/messages.pot -d locales -D messages -l en
# pybabel init -i locales/messages.pot -d locales -D messages -l uz


# pybabel extract -k _:1,1t -k _:1,2 -k __ --input-dirs=. -o locales/messages.pot
# pybabel compile -d locales -D messages
# pybabel update -d locales -D messages -i locales/messages.pot

async def main() -> None:
    # cache - MemoryStorage() -> redis
    redis = Redis()
    dp = Dispatcher(storage=RedisStorage(redis))
    bot = Bot(TOKEN)
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# https://api.telegram.org/bot7149796467:AAFUSZR2FBtqBHWGkt4Tcqj_NrCaagM4OSs/getUpdate
