import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

TOKEN = "7008756551:AAEQwgy8tRidl-EsOnZzAbk_704f9ekBzSA"

dp = Dispatcher()


def inline_buttons():
    builder = InlineKeyboardBuilder()

    for index in range(1, 11):
        builder.button(text=f"Set {index}", callback_data=f"set:{index}")

    builder.adjust(2 , repeat=True)
    return builder.as_markup()

def reply_buttons():
    builder = ReplyKeyboardBuilder()

    for index in range(1, 11):
        builder.button(text=f"Set {index}")

    builder.adjust(2 , repeat=True)
    return builder.as_markup()



@dp.message(CommandStart())
# @dp.message(Command('newbot'))
async def command_start_handler(message: Message) -> None:
    # print(message.from_user.full_name ,message.from_user.id)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=reply_buttons())
    # await message.reply(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.bot.send_message(chat_id=1458671898 , text = f"{message.from_user.username} : {message.text}")



# @dp.message(F.text.lower() != 'salom')
# @dp.message(F.text.len() != 5)
# @dp.message((F.from_user.id == 1458671898) & (F.text == 'salom'))
# @dp.message((F.from_user.id.in_({1458671898 , 234567654 , 345654})) & (F.text == 'salom'))
# @dp.message(~F.photo)
# async def salom_handler(msg: Message):
#     await msg.reply("assalom")












# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
