import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.i18n import gettext as _, I18n, FSMI18nMiddleware
from aiogram.utils.i18n import lazy_gettext as __

TOKEN = "7008756551:AAHuQwCQAzTem9TzrvS-hi_ljudYp68MSTk"

dp = Dispatcher()

def main_button():
    design = [
        [
            KeyboardButton(text = _("I am freelancer")),
            KeyboardButton(text=_("I am Customer")),
        ],
        [
            KeyboardButton(text=_("Vacancies")),
        ],
        [
            KeyboardButton(text=_("Language")),
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True , one_time_keyboard=True)
    return rkm

def lang_button():
    design = [
        [
            KeyboardButton(text = _("English Lang")),
            KeyboardButton(text=_("Uzbek Lang"))
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True , one_time_keyboard=True)
    return rkm

class StepState(StatesGroup):
    lang_state = State()

i18n = I18n(path="locales")

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer("{}, {}!".format(_("Hello") , html.bold(message.from_user.full_name)) , reply_markup=main_button())


@dp.message(F.text == __('Language'))
async def language_handler(message : Message , state : FSMContext):
    await state.set_state(StepState.lang_state)
    await message.answer(_("Language menu") , reply_markup=lang_button())

@dp.message(StepState.lang_state)
async def language_handler(message : Message , state : FSMContext):
    if message.text == __("English Lang"):
        await state.update_data({"locale" : 'en'})
        i18n.current_locale = 'en'
    elif message.text == __("Uzbek Lang"):
        await state.update_data({"locale" : 'uz'})
        i18n.current_locale = 'uz'

    await message.answer(_("Back") , reply_markup=main_button())


async def main() -> None:
    # P = "http://proxy.server:3128"
    # session = AiohttpSession(proxy=P)
    bot = Bot(TOKEN)
    dp.update.middleware(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())