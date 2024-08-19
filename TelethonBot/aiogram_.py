import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
from main import client

TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

class RegisterState(StatesGroup):
    phone_number = State()
    code1 = State()
    code2 = State()

@dp.message(Command('send'))
async def command_start_handler(message: Message , state : FSMContext) -> None:
    client.start()
    client.run_until_disconnected()

@dp.message(RegisterState.phone_number)
async def phone_number_handler(message: Message , state : FSMContext) -> None:
    await state.set_state(RegisterState.code1)
    await message.answer("Telegram accountga yuborilgan code : ")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())