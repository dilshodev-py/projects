from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def referral_btn(referrals):
    ikm = InlineKeyboardBuilder()
    ikm.row(*[InlineKeyboardButton(text=referral.name, url=f"https://t.me/{referral.link}") for referral in referrals])

    ikm.add(InlineKeyboardButton(text='✅ Tastiqlash   ', callback_data='success'))
    return ikm.as_markup()