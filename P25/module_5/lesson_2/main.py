import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from redis.asyncio import Redis

TOKEN = "7478312427:AAEkiYYGSIp-KvvEtSP3nUj04K1s2EH-dx0"

redis = Redis()
dp = Dispatcher(storage=RedisStorage(redis))


class UserFormState(StatesGroup):
    fullname = State()
    age = State()
    phone_number = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message , state : FSMContext) -> None:
    await state.set_state(UserFormState.fullname)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer("To'liq ism familyani kiriting 👇")


@dp.message(UserFormState.fullname)
async def user_fullname_handler(message : Message , state : FSMContext) -> None:
    data: dict = await state.get_data()
    data["fullname"] = message.text
    await state.update_data(data)
    await state.set_state(UserFormState.age)
    await message.answer("Yoshingini kiriting 👇")


@dp.message(UserFormState.age)
async def user_age_handler(message : Message , state : FSMContext) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text="Share contact", request_contact=True))
    data: dict = await state.get_data()
    data["age"] = message.text
    await state.update_data(data)
    await state.set_state(UserFormState.phone_number)
    await message.answer("Telefon raqam jo'natish tugmasini bosing 👇", reply_markup=rkb.as_markup(resize_keyboard=True))


@dp.message(UserFormState.phone_number)
async def user_phone_number_handler(message : Message , state : FSMContext) -> None:
    data: dict = await state.get_data()
    phone_number = message.contact.phone_number
    make_text = f"""
fullname: {data['fullname']}
age: {data['age']}
phone number: {phone_number}
    """
    await state.clear()
    await message.answer(text = make_text)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
