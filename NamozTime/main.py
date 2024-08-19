import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from sqlalchemy import select

from cron import session
from db import Namoz
from utils import parse_time, button

TOKEN = "5314436530:AAFn0f-VGeav4k-xgi7yzP8FZwdVJClY3zE"
dp = Dispatcher(storage=MemoryStorage())


class BotState(StatesGroup):
    choose = State()
@dp.message(CommandStart())
async def command_start_handler(message: Message , state : FSMContext) -> None:
    data = session.execute(select(Namoz)).fetchall()

    await state.set_data({"data" : data})
    await state.set_state(BotState.choose)
    await message.answer("Choose" , reply_markup=button(data))

@dp.message(BotState.choose)
async def choose_handler(msg : types.Message , state : FSMContext):
    data = await state.get_data()
    for i in data.get('data'):
        if i[0].name == msg.text:
            await msg.answer(text = i[0].time)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())