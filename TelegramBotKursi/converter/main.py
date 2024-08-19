import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import requests

TOKEN = "7489619129:AAGfm4h_OO83ahQPoLCZMjsELmLvENpBGoQ"


dp = Dispatcher()

class ConverterState(StatesGroup):
    converter_button = State()
    converter_money = State()
    converter = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state : FSMContext) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="USD➡️UZS"),
        KeyboardButton(text="UZS➡️USD"),

    ])
    await state.set_state(ConverterState.converter_button)
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer(
        f"""Assalomu alaykum converter botga hush kelibsiz siz bu yerda pul 
birligini boshqa pul birligiga convert qila olasiz """,
        reply_markup=rkb)

@dp.message(ConverterState.converter_button)
async def converter_button_handler(message : Message , state : FSMContext):
    from_money , to_money = message.text.split("➡️")
    await state.update_data({'from_money' : from_money , "to_money" : to_money})
    await state.set_state(ConverterState.converter_money)
    await message.answer(text = "Convert qilinadigan miqdorni kiriting !")

@dp.message(ConverterState.converter_money)
async def convert_money(message : Message , state : FSMContext):
    data = await state.get_data()
    from_money = data.get("from_money")
    to_money = data.get("to_money")
    money = float(message.text)
    response = requests.get(f'https://open.er-api.com/v6/latest/{from_money}')
    convert = response.json().get('rates').get(to_money)
    await state.clear()
    await message.answer(f"Convert : {to_money} -> {convert*money :.4f}")



async def main() -> None:
    P = "http://proxy.server:3128"
    session = AiohttpSession(proxy=P)
    bot = Bot(token=TOKEN,session=session, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
