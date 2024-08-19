from aiogram.fsm.state import StatesGroup, State


class ButtonsState(StatesGroup):
    region_buttons = State()
    workplace_buttons = State()
    change_lang = State()
    district_choose = State()
    branches_choose = State()