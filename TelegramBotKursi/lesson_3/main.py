import asyncio
import json
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import StatesGroup, State
from aiogram.methods import RevokeChatInviteLink
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "7297305631:AAHrB0bcqiAQ-K8-YaVkM3LHKju2dhOur2M"

dp = Dispatcher()


class UserForm(StatesGroup):
    fullname = State()
    age = State()
    phone_number = State()
    location = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message , state : FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await state.set_state(UserForm.fullname)
    await message.answer(f"To'liq ism familyangizni kiriting !")


@dp.message(UserForm.fullname)
async def fullname_handler(message: Message , state : FSMContext) -> None:
    await state.update_data({"fullname" : message.text})
    await state.set_state(UserForm.age)
    await message.answer("Yoshingizni kiriting !")

@dp.message(UserForm.age)
async def age_handler(message: Message , state : FSMContext) -> None:
    await state.update_data({"age" : message.text})
    await state.set_state(UserForm.phone_number)
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text = "Telefon raqam" , request_contact=True)])
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer("Telofon raqamingizni quydagi tugma orqali yuboring !" , reply_markup=rkb)

@dp.message(UserForm.phone_number)
async def phone_number_handler(message : Message , state : FSMContext):
    await state.update_data({"phone_number": message.contact.phone_number})
    await state.set_state(UserForm.location)
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text="Location", request_location=True)])
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer("Locatsiyangizni quydagi tugma orqali yuboring !" , reply_markup=rkb)

@dp.message(UserForm.location)
async def location_handler(message : Message , state : FSMContext):
    await state.update_data({'location' : {"long" : message.location.longitude , 'lat' : message.location.latitude}})
    user_data = await state.get_data()
    await state.clear()
    with open('users.json' , 'r') as f:
        users = json.load(f)
    users.append(user_data)
    with open('users.json' , 'w') as f:
        json.dump(users , f , indent=3)
    await message.answer("MOfaqiyatli malumotlaringiz saqlandi !" , reply_markup= ReplyKeyboardRemove())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
