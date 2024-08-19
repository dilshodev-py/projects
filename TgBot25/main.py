""""""
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

"""
user bot:
    .....
    
telegram bot:
    aiogram
    .....

"""

import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, CallbackQuery
from dotenv import load_dotenv
load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # rkb = ReplyKeyboardBuilder()
    # rkb.add(
    #     *[
    #         KeyboardButton(text = "+ Add Message"),
    #         KeyboardButton(text = "+ Add Question"),
    #         KeyboardButton(text = "+ Add Captcha"),
    #         KeyboardButton(text = "+ Add Veriable Input"),
    #         KeyboardButton(text = "Pagination in Editor (🔟)"),
    #         KeyboardButton(text = "🔙 Back"),
    #         KeyboardButton(text = "Main Menu"),
    #         KeyboardButton(text = "BUttons Editor"),
    #         KeyboardButton(text = "Stop Editor"),
    #         KeyboardButton(text = 'Location' , request_location=True),
    #         KeyboardButton(text = 'Phone Number' , request_contact=True)
    #       ]
    # )
    # rkb.adjust(2,2,1,2,2, 2)
    # rkb = rkb.as_markup(resize_keyboard=True)

    ikb = InlineKeyboardBuilder()
    ikb.add(
        *[
            InlineKeyboardButton(text="+ Add Message", callback_data="message"),
            InlineKeyboardButton(text="+ Add Question", callback_data="Question"),
            InlineKeyboardButton(text="+ Add Captcha", callback_data="Captcha"),
            InlineKeyboardButton(text="+ Add Veriable Input", callback_data="Input"),
            InlineKeyboardButton(text="Pagination in Editor (🔟)", callback_data="(🔟)"),
            InlineKeyboardButton(text="🔙 Back", callback_data="Back"),
            InlineKeyboardButton(text="Main Menu", callback_data="Menu"),
            InlineKeyboardButton(text="BUttons Editor", callback_data="Editor"),
            InlineKeyboardButton(text="Stop Editor", callback_data="Editor"),
            InlineKeyboardButton(text='Location', callback_data="="),
            InlineKeyboardButton(text='Phone Number', callback_data='number')
        ]
    )
    ikb.adjust(2, 2, 1, 2, 2, 2)
    ikb = ikb.as_markup(resize_keyboard=True)


    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=ikb)
    # await message.reply(f"Hello, {html.bold(message.from_user.full_name)}!")
    # await message.bot.send_message(chat_id=message.chat.id,text=f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.callback_query(F.data == 'Back')
async def back_handler(callback: CallbackQuery) -> None:
    await callback.message.answer("Orqaga degan bosildi")


@dp.message(F.contact)
async def add_message_handler(message: Message) -> None:
    await message.answer(text= message.contact.phone_number)

@dp.message(F.location)
async def location_handler(message: Message) -> None:
    await message.answer(text=f"{message.location.longitude} , {message.location.latitude}" )

# @dp.message(F.voice)
# async def photo_handler(message: Message) -> None:
#     await message.answer('Success handler')
#
#
# @dp.message(F.text == 'hello')
# async def hello_handler(message: Message) -> None:
#     await message.answer('Success handler')
#
# @dp.message(F.from_user.id == 1148477816 | F.text == 'hello')
# async def hello_handler(message: Message) -> None:
#     await message.answer('Success handler')
#
# @dp.message(F.from_user.id.in_({42, 1000, 123123}))
# async def hello_handler(message: Message) -> None:
#     await message.answer('Success handler')
#
#
# @dp.message(F.text.in_({'hello' , 'spam'}))
# async def hello_handler(message: Message) -> None:
#     await message.answer('Success handler')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
