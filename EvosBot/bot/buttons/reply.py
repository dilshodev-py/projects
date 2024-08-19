from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.buttons import text
from bot.buttons.text import back_text, ignore_text
from db.models import Region
from aiogram.utils.i18n import gettext as _


def main_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_('🏢 About company')),
        KeyboardButton(text=_('📍 Branches')),
        KeyboardButton(text=_('💼 Work Place')),
        KeyboardButton(text=_('Menu')),
        KeyboardButton(text=_('🆕 News')),
        KeyboardButton(text=_('📞 Contact/Address')),
        KeyboardButton(text=_('🇺🇿/🇷🇺/🇬🇧 Lang'))
    ])
    rkb.adjust(2,1,2,2)
    return rkb.as_markup(resize_keyboard=True)


def regions_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text = region[0]) for region in Region('name').select()
    ])
    rkb.add(
        KeyboardButton(text = ignore_text),
        KeyboardButton(text = _('🔙 Back'))
    )
    rkb.adjust(2 , repeat=True)
    return rkb.as_markup(resize_keyboard=True)

def lang_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text='🇺🇿 uz'),
        KeyboardButton(text='🇬🇧 en'),
        KeyboardButton(text='🇷🇺 ru'),
        KeyboardButton(text=_('🔙 Back')),
    ])
    rkb.adjust(3,1)
    return rkb.as_markup(resize_keyboard=True)

def make_button(list, icon=''):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=f"{icon} {i[0]}") for i in list
    ])
    rkb.add(KeyboardButton(text = _('🔙 Back')))
    rkb.adjust(2,repeat=True)
    return rkb.as_markup(resize_keyboard=True)

def make_branches_button(list, icon=''):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=f"{icon} {i[1]}") for i in list
    ])
    rkb.add(KeyboardButton(text = _('🔙 Back')))
    rkb.adjust(2,repeat=True)
    return rkb.as_markup(resize_keyboard=True)



