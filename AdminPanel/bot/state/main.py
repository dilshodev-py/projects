from aiogram.fsm.state import StatesGroup, State


class SubjectState(StatesGroup):
    insert = State()
    delete = State()
    update = State()
    read = State()
    name = State()
