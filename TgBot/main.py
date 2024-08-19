"""
telegram api
    telegram bot api
        aiogram
        pytelegramBot
        TeleBot
        Pyrogram
        ...
    user bot api
        telethon
        Pyrogram

"""
# pip3 install aiogram
# pip install aiogram
import asyncio
import json
import logging
import sys

import aiofiles
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7094745454:AAHCARfumjUFIvzgnjsbROkI7qNmAi4Vr-8"  # BotFather

dp = Dispatcher()


# @dp.message(CommandStart())
# async def echo_handler(message: Message) -> None:
#     await message.reply('salom')
#
#
# @dp.message(F.text.startswith('u'))
# async def u_handler(message: Message):
#     await message.reply("u handler ishladi !")
#
#
# @dp.message(F.content_type.in_('voice'))
# async def voice_handler(message: Message):
#     await message.answer_voice(message.voice.file_id)
#
#
# @dp.message(lambda message: [m for m in message.text if m in '1234567890'])
# async def number_handler(message: Message):
#     await message.answer('number handler ishladi')


# @dp.message(F.text == 'botir')
# async def botir_handler(message: types.Message):
# await message.reply()
# await message.answer()
# print(message.from_user.id)
# await message.bot.send_message(1148477816 , message.text)


# ====================== tasks =======================

# phone_number handler
#     phone save to json filega


# contact handler
#     phone save to json filega


# 10 + (67- 100) handler

# python.py handler

# photo handler

# bot dan foydalanyotgan odamlarni malumotlarini jsonga saqlimiz
#     id
#     first_name
#     last_name
#     username
#     username

# command /reklama
#     reklama message all user send


# chat Bot
# /start
#     username kiriting # botir:
#     botir:

async def save_phone_number(phone_number):
    async with aiofiles.open('phone_numbers.json', "r") as f:
        data: str = await f.read()
        data: list = json.loads(data)
    data.append(phone_number)
    async with aiofiles.open('phone_numbers.json', "w") as f:
        data = json.dumps(data, indent=3)
        await f.write(data)


async def save_user(user: dict):
    async with aiofiles.open('users.json', "r") as f:
        users: str = await f.read()
        users: list = json.loads(users)
    for u in users:
        if user.get("id") == u.get('id'):
            break
    else:
        users.append(user)
        async with aiofiles.open('users.json', "w") as f:
            data = json.dumps(users, indent=3)
            await f.write(data)

async def get_users():
    async with aiofiles.open('users.json', "r") as f:
        users: str = await f.read()
        users: list = json.loads(users)
    return users

@dp.message(CommandStart())
async def start_handler(message: Message):
    user = {
        'id' : message.from_user.id,
        'first_name' : message.from_user.first_name,
        'last_name' : message.from_user.last_name,
        'username' : message.from_user.username,
    }
    await save_user(user)

@dp.message((F.from_user.id == 1148477816) & (F.text.startswith('/reklama :')))
async def send_reklama_handler(message: Message):
    users: list[dict] = await get_users()
    reklama_text = message.text.split('/reklama :')[1]
    for user in users:
        user_id = user.get('id')
        await message.bot.send_message(user_id , reklama_text)

@dp.message((F.text.startswith("+9989")) & (F.text.len() == 13) & (F.text[1:].isdigit()))
@dp.message(F.content_type.in_('contact'))
async def phone_number_handler(message: Message):
    if message.contact:
        await save_phone_number(message.contact.phone_number)
    else:
        await save_phone_number(message.text)


@dp.message(
    lambda msg: False if not msg.text else bool([i for i in msg.text if i in ['+', '-', '*', "/", "(", ")", "**"]]))
async def calculator_handler(message: Message):
    try:
        result = str(eval(message.text))
        await message.reply(result)
    except:
        await message.reply("matematik ifodada xato bor !")


@dp.message((F.document) & (F.document.file_name.endswith('.py')))
async def file_handler(message: Message):
    await message.reply('BU file python file !')

@dp.message(F.photo)
async def photo_handler(message : Message):
    await message.reply_photo(message.photo[0].file_id)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)
    # webhook


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


"""
#tg bot vedioni korish


# phone_number handler
#     phone save to json filega  


# contact handler
#     phone save to json filega


# 10 + (67- 100) handler

# python.py handler
    bu python file!

# photo handler

# bot dan foydalanyotgan odamlarni malumotlarini jsonga saqlimiz
#     id
#     first_name
#     last_name
#     username

# command /reklama : 
#     reklama message all user send


# chat Bot
# /start
#     username kiriting # botir:
#     botir:
"""
