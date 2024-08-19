from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_crud_btn(pos):
    s_insert = InlineKeyboardButton(text="Insert", callback_data=f"insert_{pos}")
    s_read = InlineKeyboardButton(text="Read", callback_data=f"read_{pos}")
    s_update = InlineKeyboardButton(text="Update", callback_data=f"update_{pos}")
    s_delete = InlineKeyboardButton(text="Delete", callback_data=f"delete_{pos}")
    s_back = InlineKeyboardButton(text="⬅️back", callback_data=f"back_{pos}")
    return InlineKeyboardMarkup(inline_keyboard=[[s_insert, s_read],[s_update, s_delete], [s_back]], resize_keyboard=True)


def subject_list_btn(subjects : list[tuple]):
    design = []
    row = []
    for subject in subjects:
        row.append(InlineKeyboardButton(text = subject[1], callback_data=f"subject_{subject[0]}"))
        if len(row) == 2:
            design.append(row)
            row = []
    else:
        if row:
            design.append(row)
    design.append([InlineKeyboardButton(text = "⬅️back",callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=design)



