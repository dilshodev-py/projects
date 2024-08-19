import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "7297305631:AAHrB0bcqiAQ-K8-YaVkM3LHKju2dhOur2M"

dp = Dispatcher()


# /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # await message.answer(text = 'Hello World')
    await message.reply(text='Hello World')


# /menu
@dp.message(Command('menu'))
async def menu_handler(message: Message) -> None:
    await message.answer("Menu bo'limiga hush kelibsiz !")


@dp.message(Command('help'))
async def menu_handler(message: Message) -> None:
    await message.answer("Help bo'limiga hush kelibsiz !")


@dp.message(F.photo)
async def photo_handler(message: Message) -> None:
    await message.answer("Bu xabar rasm ko'rinishida !")


@dp.message(F.text == 'hello')
async def hello_handler(message: Message) -> None:
    await message.answer(text="Hi !")


@dp.message((F.text == 'admin') & (F.from_user.id == 1148477816))
async def from_user_handler(message: Message) -> None:
    await message.answer(text="1148477816 user xabar yubordi")


# Assalomu Alaykum
@dp.message(F.text == 'Assalomu Alaykum')
async def hello_handler(message: Message) -> None:
    # await message.answer(text = "Valekum Assalom")
    await message.reply(text="Valekum Assalom")


# @dp.message(F.text != 'kitob')
# async def kitob_handler(message: Message) -> None:
#     await message.answer(text="Bu habar kitob so'ziga teng emas !")


# /reply_button
@dp.message(Command('reply_button'))
async def reply_button_handler(message: Message) -> None:
    design = [
        [
            KeyboardButton(text='What are your hours ?⏳'),
            KeyboardButton(text='Can I track my order? 📦')
        ],
        [
            KeyboardButton(text='How Do i report a problem?')
        ]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    await message.answer("Quydagi So'rovlardan birini tanlang !", reply_markup=rkm)

@dp.message(Command('inline_button'))
async def inline_button_handler(message: Message) -> None:
    design = [
        [
            InlineKeyboardButton(text='John' , callback_data='john'),
            InlineKeyboardButton(text='❌' ,callback_data='x1' )
        ],
        [
            InlineKeyboardButton(text='Python' , callback_data='python'),
            InlineKeyboardButton(text='❌' ,callback_data='x2' )
        ],
        [
            InlineKeyboardButton(text='pyTegramBotAPI', callback_data='tg_python'),
            InlineKeyboardButton(text='❌', callback_data='x3')
        ]
    ]
    rkm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer("Quydagi So'rovlardan birini tanlang !", reply_markup=rkm)

# @dp.message(F.from_user.id.in_({1148477816, 765432345, 23456, 3456, 23456}))
# async def kitob_handler(message: Message) -> None:
#     await message.answer(text="Bu habar kitob so'ziga teng emas !")


@dp.message(Command('phone_number'))
async def phone_number_handler(message: Message) -> None:
    design = [
        [
            KeyboardButton(text = "Phone Click ☎️", request_contact=True),
            KeyboardButton(text = "Location 📍️", request_location=True)
        ]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)
    await message.answer('Telefon raqamni Yuborish uchun quydagi buttondi bosing !', reply_markup=rkm)

@dp.message(F.contact)
async def contact_handler(message: Message) -> None:
    await message.answer(text = message.contact.phone_number)

@dp.message(F.location)
async def location_handler(message: Message) -> None:
    await message.answer(text = f"{message.location.latitude} , {message.location.longitude}")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
