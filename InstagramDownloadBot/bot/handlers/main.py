from typing import Optional

import instaloader
from aiogram import F
from aiogram.enums import ChatMemberStatus
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from bot.buttons.inlines import referral_btn
from bot.dispatcher import dp
from db import User
from db.models.users import Referal




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user: Optional[User] = await User.get(id_=message.from_user.id)
    if user is None:
        user = {"id": message.from_user.id, "username": message.from_user.username,  # noqa
                "full_name": f"{message.from_user.full_name}", "lang": User.LangEnum('en')}  # noqa
        await User.create(**user)  # noqa
    referrals = await Referal.get_all()
    l = []
    for i, referral in enumerate(referrals):
        chat = await message.bot.get_chat("@"+referral.link)
        chat_member = await message.bot.get_chat_member(chat.id, message.from_user.id,request_timeout=1)
        if chat_member.status == ChatMemberStatus.LEFT:
            l.append(referral)
    if l:
        await message.answer("Quydagi kannal guruhlarga azo bo'ling",
                         reply_markup=(await referral_btn(l)))
    else:
        await message.answer("Instagram ga tegishli video linklaridan yuboring")


@dp.callback_query(F.data.startswith('success'))
async def success_handler(query: CallbackQuery) -> None:
    referrals = await Referal.get_all()
    l = []
    for i, referral in enumerate(referrals):
        chat = await query.bot.get_chat("@"+referral.link)
        chat_member = await query.bot.get_chat_member(chat.id, query.from_user.id,request_timeout=1)
        if chat_member.status == ChatMemberStatus.LEFT:
            l.append(referral)
    if l:
        await query.answer("Hali to'liq azo bo'lmadingiz !")
    else:
        await query.message.delete()
        await query.message.answer("Instagram ga tegishli video linklaridan yuboring")




