from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.buttons.text import teachers, students, groups, subjects


def admin_menu_btn():
    teachers_btn = KeyboardButton(text=teachers)
    students_btn = KeyboardButton(text=students)
    groups_btn = KeyboardButton(text=groups)
    subjects_btn = KeyboardButton(text=subjects)
    return ReplyKeyboardMarkup(keyboard=[[students_btn,teachers_btn],
                                         [groups_btn, subjects_btn]], resize_keyboard=True)



