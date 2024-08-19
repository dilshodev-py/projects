from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.buttons.reply import main_menu_btn
from bot.dispatcher import router

@router.message(CommandStart())
async def lang_handler(message: Message):
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[
        KeyboardButton(text=_("Uzbek 🇺🇿")),
        KeyboardButton(text=_("English 🇬🇧"))
    ])
    await message.answer(_("Choose language"), reply_markup=rkm.as_markup(resize_keyboard=True))

@router.message(F.text.in_([__("Uzbek 🇺🇿") , __("English 🇬🇧")]))
async def uzb_handler(message: Message, state: FSMContext):
    lang = "uz" if message.text == __("Uzbek 🇺🇿") else "en"
    await state.update_data({"locale": lang})
    await message.answer_photo(photo="https://telegra.ph/file/086ffbb8eb927c7eead39.png" , reply_markup=main_menu_btn())


