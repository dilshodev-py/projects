import asyncio
import json
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from aiogram.utils.markdown import hbold

TOKEN = "7149796467:AAEiHpUDQYQTc64ONrzOloAp4KWOMbZECJQ"

dp = Dispatcher()
# https://telegra.ph/file/f57b8dbc41dc656508ad1.png
def buttons():
    btn1 = KeyboardButton(text = "Location" , request_location=True)
    btn2 = KeyboardButton(text = "Contact" , request_contact=True)
    btn3 = KeyboardButton(text = "btn3")
    design = [
        [btn1 , btn2],
        [btn3],
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def inline_buttons():
    btn1 = InlineKeyboardButton(text = "btn1" , callback_data="1")
    btn2 = InlineKeyboardButton(text = "btn2" , callback_data='2')
    btn3 = InlineKeyboardButton(text = "btn3" , callback_data="3")
    design = [
        [btn1 , btn2],
        [btn3],
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)
# btn1     btn2
#     btn3

@dp.message(CommandStart())
async def start_handler(message:Message):
    await message.answer("Hello" , reply_markup=inline_buttons())

@dp.message(lambda message : message.text == "btn1")
async def btn1_handler(message: Message):
    await message.answer("Button 1 bosildi")

@dp.message(lambda message : message.text == "btn2")
async def btn1_handler(message: Message):
    await message.answer("Button 2 bosildi")

@dp.message(lambda message : message.text == "btn3")
async def btn1_handler(message: Message):
    await message.answer("Button 3 bosildi")

# @dp.callback_query(lambda call : call.data == "1")
# async def btn1_handler(call : CallbackQuery):
#     await call.message.answer_location()


@dp.message(F.contact)
async def contact_handler(message:Message):
    await message.answer(text = message.contact.phone_number)





# @dp.message(CommandStart())
# @dp.message(Command('photo'))
# async def command_start_handler(message: Message) -> None:
#     await message.answer_photo(photo = "https://telegra.ph/file/a249e0df12b80e55dbcd6.png")


    # await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    # await message.reply(f"Hello, {hbold(message.from_user.full_name)}!")
    # await message.bot.send_message(chat_id= 6410862700, text = f"Hello, {hbold(message.from_user.full_name)}!")

# @dp.message(lambda message : message.text == "botir")
# async def botir_handler(message: Message):
#     await message.answer("Salom")
#
# @dp.message(F.video)
# async def photo_handler(message :Message):
#     await message.bot.send_photo(chat_id=6410862700 , photo=message.photo[0].file_id)
#
# @dp.message(F.photo)
# @dp.message(F.message, lambda message : message.text.isdigit() , lambda message : int(message.text) % 2 == 0)
# async def juft_handler(message: Message):
#     await message.answer("Juft son")
#


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

