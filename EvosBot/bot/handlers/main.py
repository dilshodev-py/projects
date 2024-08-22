from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.buttons.reply import main_buttons
from bot.buttons.text import compony_about_text, back_text, ignore_text
from bot.state import ButtonsState
from db.models import User, SiteSetting
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _

main_router = Router()






@main_router.message(ButtonsState.region_buttons, F.text == __('❌ Ignore ❌'))
@main_router.message(ButtonsState.change_lang, F.text == __('🔙 Back'))
@main_router.message(ButtonsState.region_buttons, F.text == __('🔙 Back'))
@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    user = User().select(user_id=message.from_user.id)
    if not user:
        User(
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            lang=message.from_user.language_code,
        ).insert()

    logo_photo = 'AgACAgQAAxkDAAPNZr3sz8rWUQ1lWPBfsKZ4Ty-pngsAAjC2MRtzo_VR3q6veGl9ge8BAAMCAANzAAM1BA'
    # await message.answer_photo(photo=FSInputFile('/home/dilshod/PycharmProjects/EvosBot/img.png', 'rasm'))
    # await message.answer_photo(photo='https://telegra.ph/file/3d75e7593b04a72018e59.png')
    await message.answer_photo(photo=logo_photo, reply_markup=main_buttons())


@main_router.message(F.text == __('🏢 About company'))
async def main_menu_handler(message: Message, state: FSMContext) -> None:
    site_data = SiteSetting().select()
    if site_data:
        site_data = site_data[0]
        await message.answer_photo(photo=site_data[-1], caption=site_data[-2], reply_markup=main_buttons())
