from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __, I18n

from bot.buttons.reply import lang_buttons, main_buttons
from bot.state import ButtonsState

language_router = Router()

@language_router.message(F.text == __('🇺🇿/🇷🇺/🇬🇧 Lang'))
async def language(message: Message, state : FSMContext):
    await state.set_state(ButtonsState.change_lang)
    await message.answer(_("Choose language") , reply_markup=lang_buttons())

@language_router.message(ButtonsState.change_lang , F.text.in_({"🇺🇿 uz", "🇬🇧 en", "🇷🇺 ru"}))
async def language(message: Message, state : FSMContext, i18n : I18n):
    lang = message.text.split()[-1]
    await state.update_data({"locale" : lang})
    i18n.current_locale = lang
    await message.answer(_("Change language") , reply_markup=main_buttons())



