from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.buttons.reply import regions_button, make_button, make_branches_button, main_buttons
from bot.buttons.text import work_place_text, back_text
from bot.state import ButtonsState
from db.models import Region
from dispatcher import dp
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _


@dp.message(ButtonsState.workplace_buttons , F.text == __('🔙 Back'))
@dp.message(F.text == work_place_text)
async def work_place(message: Message , state : FSMContext):
    await state.set_state(ButtonsState.region_buttons)
    await message.answer(text = _("Join the EVOS team!"))
    await message.answer(text = _("📍 Select a city."), reply_markup= regions_button())


@dp.message(ButtonsState.district_choose , F.text == __('🔙 Back'))
@dp.message(ButtonsState.region_buttons)
async def work_place(message: Message , state : FSMContext):
    region_name = message.text
    if message.text == __('🔙 Back'):
        data = await state.get_data()
        region_name = data['region']
    work_place_list = Region().work_place_list(region_name)
    if not work_place_list:
        await message.answer("Bo'sh ish o'rni mavjud emas", reply_markup=regions_button())
    else:
        await state.update_data({"region" : region_name})
        await message.answer("Ish o'rnidan tanlang" , reply_markup=make_button(work_place_list))
        await state.set_state(ButtonsState.workplace_buttons)


@dp.message(ButtonsState.branches_choose , F.text == __('🔙 Back'))
@dp.message(ButtonsState.workplace_buttons)
async def work_place_handler(message: Message , state : FSMContext):
    await state.set_state(ButtonsState.district_choose)
    data = await state.get_data()
    workplace_name = message.text
    if message.text == __('🔙 Back'):
        workplace_name = data['workplace']
    await state.update_data({"workplace" : workplace_name})
    d_list = Region().district_list(data.get('region'), workplace_name)
    await message.answer("O'zizga qulay tumandi tanlang !" , reply_markup=make_button(d_list))


@dp.message(ButtonsState.district_choose)
async def district_handler(message: Message , state : FSMContext):
    await state.set_state(ButtonsState.branches_choose)
    data = await state.get_data()
    district_name = message.text
    b_list = Region().branches_list(data['region'], data['workplace'],district_name)
    await state.update_data({'branches_list' : b_list})
    await message.answer("O'zizga qulay filialni tanlang !" , reply_markup=make_branches_button(b_list , icon="📍"))


@dp.message(ButtonsState.branches_choose)
async def branches_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    branches_name = message.text
    choose_branche = []
    for branche in data['branches_list']:
        if branches_name == f"📍 {branche[1]}":
            choose_branche = branche
    await state.update_data({"locale" : data['locale'] })

    await message.answer_photo(photo = choose_branche[-1], caption=choose_branche[4]) # noqa
    await message.answer_location(longitude=choose_branche[2] , latitude=choose_branche[3], reply_markup=main_buttons())

