import asyncio
import logging
import sys
from typing import Callable, Dict, Any, Awaitable

from aiogram import Bot, Dispatcher, html, Router, F, BaseMiddleware
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.i18n import ConstI18nMiddleware
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiohttp.typedefs import Middleware
from redis.asyncio import Redis

from module_5.lesson_2.home_work.ORM import Member

TOKEN = "7008756551:AAFDm71K9ggvA7nGNBerxh0wotp0jHFwVvE"


main_router = Router()


register_text = "Register ®️"
login_text = "Login"


class RegisterState(StatesGroup):
    fullname = State()
    phone_number = State()
    location = State()
    username = State()
    password = State()


class LoginState(StatesGroup):
    username = State()
    password = State()


class MainState(StatesGroup):
    main_menu = State()


async def login_register_button():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[KeyboardButton(text=login_text), KeyboardButton(text=register_text)])
    rkm.adjust(2)
    rkm = rkm.as_markup(resize_keyboard=True)
    return rkm

@main_router.message(CommandStart())
async def command_start_handler(message: Message ) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=await login_register_button())
    await message.answer("Buttonlardan birini tanlang")

@main_router.message(F.text == register_text)
async def register_handler(message: Message, state: FSMContext):
    await state.set_state(RegisterState.fullname)
    await message.answer("Fullname: ", reply_markup=ReplyKeyboardRemove())


async def phone_button():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[KeyboardButton(text="contact share", request_contact=True)])
    rkm = rkm.as_markup(resize_keyboard=True)
    return rkm


async def location_button():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[KeyboardButton(text="Location", request_location=True)])
    rkm = rkm.as_markup(resize_keyboard=True, one_time_keyboard=True)
    return rkm


@main_router.message(RegisterState.fullname)
async def fullname_handler(message: Message, state: FSMContext):
    await state.update_data({"fullname": message.text})
    await state.set_state(RegisterState.phone_number)
    rkm = await phone_button()
    await message.answer("Telefon raqam yuborish u-n pasdegi tugmani bosing !", reply_markup=rkm)


@main_router.message(RegisterState.phone_number, F.contact)
async def phone_number_handler(message: Message, state: FSMContext):
    await state.update_data({'phone_number': message.contact.phone_number})
    await state.set_state(RegisterState.location)
    rkm = await location_button()
    await message.answer("Location yuborish u-n pasdegi tugmani bosing !", reply_markup=rkm)


@main_router.message(RegisterState.location, F.location)
async def location_handler(message: Message, state: FSMContext):
    await state.update_data({'longitude': message.location.longitude, 'latitude': message.location.latitude})
    await state.set_state(RegisterState.username)
    await message.answer("Username kiriting : ", reply_markup=ReplyKeyboardRemove())


@main_router.message(RegisterState.username, F.text)
async def username_handler(message: Message, state: FSMContext):
    await state.update_data({'username': message.text})
    await state.set_state(RegisterState.password)
    await message.answer("Password kiriting : ")


@main_router.message(RegisterState.password, F.text)
async def password_handler(message: Message, state: FSMContext):
    await state.update_data({"password": message.text})
    data = await state.get_data()
    await state.clear()
    await message.answer(f"Malumotlariz :\n {str(data)}", reply_markup=await login_register_button())



# ========================= login =======================

@main_router.message(F.text == login_text)
async def register_handler(message: Message, state: FSMContext):
    await state.set_state(LoginState.username)
    await message.answer("Username: ", reply_markup=ReplyKeyboardRemove())

@main_router.message(LoginState.username, F.text)
async def username_handler(message: Message, state: FSMContext):
    await state.update_data({"username" : message.text})
    await state.set_state(LoginState.password)
    await message.answer("Password: ", reply_markup=ReplyKeyboardRemove())

@main_router.message(LoginState.password, F.text)
async def username_handler(message: Message, state: FSMContext):
    password = message.text
    data = await state.get_data()
    user = Member().select(username = data.get('username') , password = password)
    if user:
        await message.answer("Success !", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Not found account", reply_markup=ReplyKeyboardRemove())

    await state.clear()
    await message.answer("FInish !", reply_markup=ReplyKeyboardRemove())



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    redis = Redis()
    dp = Dispatcher(storage=RedisStorage(redis))
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
