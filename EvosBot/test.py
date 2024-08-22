# import asyncio
# import logging
# import sys
# from os import getenv
#
# from aiogram import Bot, Dispatcher, html, F
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message, KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
#
# TOKEN = "7507461491:AAF8fnCzU9YTABItpIx3HIqw1JHsXIVQhfc"
#
# dp = Dispatcher()
#
#
# class ButtonsState(StatesGroup):
#     sub_menu = State()
#     sub_sub_menu = State()
#
# @dp.message(ButtonsState.sub_menu , F.text == "back")
# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text = "menu1"))
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=rkb)
#
#
# @dp.message(ButtonsState.sub_sub_menu , F.text == "back")
# @dp.message(F.text == "menu1")
# async def command_start_handler(message: Message, state : FSMContext) -> None:
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(*[
#         KeyboardButton(text = "1.1"),
#         KeyboardButton(text = "1.2"),
#         KeyboardButton(text = "1.3"),
#         KeyboardButton(text = "back")
#     ])
#     rkb.adjust(3,1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(ButtonsState.sub_menu)
#     await message.answer("Sub menu", reply_markup=rkb)
#
# @dp.message(ButtonsState.sub_menu,F.text == "1.1")
# async def command_start_handler(message: Message, state : FSMContext) -> None:
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(*[
#         KeyboardButton(text = "1.1.1"),
#         KeyboardButton(text = "1.1.2"),
#         KeyboardButton(text = "1.1.3"),
#         KeyboardButton(text = "back")
#     ])
#     rkb.adjust(3,1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(ButtonsState.sub_sub_menu)
#     await message.answer("Sub menu", reply_markup=rkb)
#
# @dp.message(ButtonsState.sub_menu,F.text == "1.2")
# async def command_start_handler(message: Message, state : FSMContext) -> None:
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(*[
#         KeyboardButton(text = "1.2.1"),
#         KeyboardButton(text = "1.2.2"),
#         KeyboardButton(text = "1.2.3"),
#         KeyboardButton(text = "back")
#     ])
#     rkb.adjust(3,1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(ButtonsState.sub_sub_menu)
#     await message.answer("Sub menu", reply_markup=rkb)
#
#
#
# async def main() -> None:
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
#
#
# """
# /start:
#     menu1
#
# menu1:
#     1.1     1.2     1.3
#             back
#
# 1.1:
#     1.1.1      1.1.2      1.1.3
#             back
# 1.2:
#     1.2.1    1.2.2        1.2.3
#             back
#
#
#
#
#
# """
# import asyncio
# from pprint import pprint
#
# import httpx
#
#
#
# async def get_products():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://dummyjson.com/products')
#     return response.json().get('products')
#
#
# pprint(asyncio.run(get_products()))


# <-   0   ->
# calculator
# evos menu page