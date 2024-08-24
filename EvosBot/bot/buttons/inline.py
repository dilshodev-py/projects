from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from db.models import Category


async def category_inline_button():
    ikb = InlineKeyboardBuilder()
    ikb.add(*[
        InlineKeyboardButton(text=category.name , callback_data=str(category.id)) for category in Category('id' , 'name').select()
    ])
    ikb.add(
        InlineKeyboardButton(text = "Qidiruv 🔎" , switch_inline_query_current_chat="")
    )
    ikb.adjust(2 , repeat=True)
    return ikb.as_markup()

async def product_inline_button(page_num ,count=0):
    ikb = InlineKeyboardBuilder()
    ikb.add(*[
        InlineKeyboardButton(text="⬅️" , callback_data=f"pagination_{page_num-1}"),
        InlineKeyboardButton(text="➡️" , callback_data=f"pagination_{page_num+1}"),
        InlineKeyboardButton(text="➖" , callback_data=f"minus_{count-1}"),
        InlineKeyboardButton(text=f"{count}" , callback_data="count"),
        InlineKeyboardButton(text="➕" , callback_data=f"plus_{count+1}"),
        InlineKeyboardButton(text="delete 🗑" , callback_data=f"delete"),
        InlineKeyboardButton(text="⬅️ back", callback_data=f"back"),
        InlineKeyboardButton(text="🛒 add ✅" , callback_data=f"add"),
    ])
    ikb.adjust(2, 3  ,1 , 2)
    return ikb.as_markup()


