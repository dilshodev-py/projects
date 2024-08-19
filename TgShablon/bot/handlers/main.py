from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from bot.dispatcher import dp
from db.models import User


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = {
        "user_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username
    }
    user = User(**user)
    if not user.select(user_id = message.from_user.id):
        user.insert()
    await message.answer(_("Hello, {name}!").format(name=html.quote(message.from_user.full_name)))



