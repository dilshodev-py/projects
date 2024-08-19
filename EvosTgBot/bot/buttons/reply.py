from aiogram.types import KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# company_text = _("🏢 About Company")
# branch_text = _("📍 Branches")
# vacancy_text = _("💼 Vacancy")
# menu_text = _("🍽 Menu")
# news_text = _("🗣  News")
# contact_text = _("☎️Contact/Location")
# lang_text = _("🇺🇿/🇬🇧 lang")

def main_menu_btn():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[
        KeyboardButton(text = _("🏢 About Company")),
        KeyboardButton(text = _("📍 Branches")),
        KeyboardButton(text = _("💼 Vacancy")),
        KeyboardButton(text = _("🍽 Menu")),
        KeyboardButton(text = _("🗣  News")),
        KeyboardButton(text = _("☎️Contact/Location")),
        KeyboardButton(text = _("🇺🇿/🇬🇧 lang"))
    ])
    rkm.adjust(2 , 1 , 2 , 2)
    return rkm.as_markup(resize_keyboard = True)
