import asyncio
import json
import logging
import sys

import aiofiles
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = "7094745454:AAHCARfumjUFIvzgnjsbROkI7qNmAi4Vr-8"  # BotFather

dp = Dispatcher()

users = {}


async def save_user(message):
    user = {
        'id': message.from_user.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
    }
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


async def boy_users():
    usernames = []
    for chat_id , info in users.items():
        if info.get('gender') == 'M':
            usernames.append(info.get("username"))
    return usernames

def boy_girl_usernames():
    usernames = []
    for chat_id, info in users.items():
        usernames.append(info.get("username"))
    return usernames

async def search_user(username):
    for chat_id , info in users.items():
        if info.get("username") == username:
            return chat_id

admin_id = 12345678

# TODO 1 users save to json file
# TODO 2 username unique
# TODO 3 /girls
# TODO 4 /reklama (if admin)




@dp.message(CommandStart())
async def start_handler(message: Message):
    await save_user(message)
    users.update({message.from_user.id : {}})
    await message.answer("Username kiriting (username: admin) : ")

# state
@dp.message(F.text.startswith('username:'))
async def username_handler(message: Message):
    users[message.from_user.id]['username'] = message.text.split('username:')[1].strip()
    await message.answer("Gender M/F : ")

@dp.message((F.text == 'M') | (F.text == 'F'))
async def gender_handler(message : Message):
    users[message.from_user.id]['gender'] = message.text
    text = """
        kimni qidiryabsiz ?
        /boy 
        /girl"""
    await message.answer(text)

@dp.message(Command('boy'))
async def boys_username(message : Message):
    usernames = await boy_users()
    text = "\n".join(usernames)
    await message.answer(text)

@dp.message(lambda msg : msg.text.split(':')[0].strip() in boy_girl_usernames())
async def send_message(message : Message):
    username = message.text.split(':')[0].strip()
    send_username = users[message.from_user.id]['username']
    message_text = f"{send_username}: {message.text.split(':')[1].strip()}"
    recever_id = await search_user(username)
    await message.bot.send_message(recever_id , message_text)






async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
