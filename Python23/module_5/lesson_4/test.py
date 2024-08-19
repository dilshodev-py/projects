import asyncio
import json
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto

TOKEN = "7008756551:AAHuQwCQAzTem9TzrvS-hi_ljudYp68MSTk"

dp = Dispatcher()


def pagination_btn(product_index , max_len):

    design = [
        [
            InlineKeyboardButton(text='prev', callback_data=f'prev_{product_index - 1}'),
            InlineKeyboardButton(text = str(product_index+1) , callback_data=f'session_{product_index}'),
            InlineKeyboardButton(text = 'next' , callback_data=f'next_{product_index+1}'),
        ]
    ]
    if product_index == 0:
          del design[0][0]
    if max_len <= product_index+1:
        del design[0][2]
    return InlineKeyboardMarkup(inline_keyboard=design)

def buy_btn(product_id):

    design = [
        [
            InlineKeyboardButton(text='buy', callback_data=f'product_{product_id}'),
            InlineKeyboardButton(text='back', callback_data=f'back_{product_id-1}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=design)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.text.split()[1]
    await message.answer(text = user_id)


@dp.message(Command('products'))
async def command_start_handler(message: Message , state : FSMContext) -> None:
    with open('products.json' , 'r') as f:
        products: list[dict] = json.load(f)
    await state.update_data({'products': products})
    first_product = products[0]
    max_len = len(products)
    product_index = 0
    caption = f"""
Title : {first_product.get('title')}
Price : {first_product.get('price')}
    """
    await message.answer_photo(photo=first_product.get('images')[0] , caption=caption , reply_markup= pagination_btn(product_index, max_len) )

@dp.callback_query((F.data.startswith('next_')) | (F.data.startswith('prev_')) | (F.data.startswith('back_')))
async def next_handler(callback : CallbackQuery , state : FSMContext):
    product_index = int(callback.data.split("_")[1])
    data = await state.get_data()
    products = data.get('products')
    max_len = len(products)
    session_product = products[product_index]
    caption = f"""
    Title : {session_product.get('title')}
    Price : {session_product.get('price')}
        """
    await callback.message.edit_media(media=InputMediaPhoto(media = session_product.get('images')[0] , caption=caption),
                               reply_markup=pagination_btn(product_index , max_len))


@dp.callback_query(F.data.startswith('session_'))
async def next_handler(callback : CallbackQuery , state : FSMContext):
    product_index = int(callback.data.split("_")[1])
    data = await state.get_data()
    products = data.get('products')

    session_product = products[product_index]
    caption = f"""
Title : {session_product.get('title')}
Description : {session_product.get('description')}
Price : {session_product.get('price')}"""
    await callback.message.edit_caption( caption=caption,
                               reply_markup=buy_btn(session_product.get('id')))


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())