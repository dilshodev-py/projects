from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from bot.buttons.reply import admin_menu_btn
from dispatcher import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=admin_menu_btn())


