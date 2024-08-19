import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('music', prefix='$'))
async def music_command_handler(message: Message) -> None:
    await message.answer_audio('CQACAgIAAxkBAAMPZr9yl4KKL7f3h9Hub6IzNCgPIJcAApEUAAI_8olLu0qwNG34-pQ1BA')


@dp.message(F.photo)
async def photo_command_handler(message: Message) -> None:
    await message.reply('Rasm Yuborildi')
    await message.answer('Solehga Rasm Yuborildi')
    await message.bot.send_photo(chat_id=1300817834 , photo=message.photo[0].file_id)


@dp.message(F.text == "hello")
async def text_command_handler(message: Message) -> None:
    await message.reply('Hello World')


@dp.message(F.text.in_({"hello" , "salom" , "hi"}) )
async def text_command_handler(message: Message) -> None:
    await message.reply('Hello World')

@dp.message(Command("reply_button") )
async def text_command_handler(message: Message) -> None:
    rkb = ReplyKeyboardBuilder()

    rkb.add(
        KeyboardButton(text = '📚 Books1'),
        KeyboardButton(text = '📚 Books2'),
        KeyboardButton(text = '📚 Books3'),
        KeyboardButton(text = '📚 Books4'),
        KeyboardButton(text = '📚 Books5'),
        KeyboardButton(text = 'Location', request_location=True),
        KeyboardButton(text = 'Phone Number', request_contact=True),
    )
    rkb.adjust(1,1,2,1,2)
    rkb= rkb.as_markup(resize_keyboard=True)
    await message.reply('Menyu' , reply_markup=rkb)


@dp.message(Command("inline_button") )
async def text_command_handler(message: Message) -> None:
    rkb = InlineKeyboardBuilder()

    rkb.add(
        InlineKeyboardButton(text = '📚 Books1' , callback_data='1'),
        InlineKeyboardButton(text = '📚 Books2', callback_data='2'),
        InlineKeyboardButton(text = '📚 Books3', callback_data='3'),
        InlineKeyboardButton(text = '📚 Books4', callback_data='4'),
        InlineKeyboardButton(text = '📚 Books5', callback_data='5'),
        InlineKeyboardButton(text = 'Kun uz', url='https://kun.uz'),
    )
    rkb.adjust(1,1,2,1)
    rkb= rkb.as_markup(resize_keyboard=True)
    await message.reply('Menyu' , reply_markup=rkb)


@dp.callback_query(F.data == '1')
async def inline_command_handler(callback: CallbackQuery) -> None:
    await callback.message.answer(text = "1 - button bosildi")




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())