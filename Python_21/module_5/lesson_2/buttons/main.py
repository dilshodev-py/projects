import asyncio
import json
import logging
import sys

import aiofiles
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, KeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

TOKEN = "7169306709:AAE9Vydeu8VHBJxFsz3QG9Uq2eGLtOcjucE"

dp = Dispatcher()
# pip install aiohttp_socks

async def region_markup():
    async with aiofiles.open("/home/dilshod/PycharmProjects/Python_21/module_5/lesson_2/buttons/regions.json", "r",encoding='utf-8') as f:
        data = await f.read()
        regions = json.loads(data)
    buttons = []
    for region in regions:
        btn = InlineKeyboardButton(text=region.get("name_uz"), callback_data="region_" + region.get("id"))
        buttons.append(btn)

    markup = InlineKeyboardBuilder()
    markup.add(*buttons)
    markup.adjust(2, repeat=True)
    markup = markup.as_markup()
    return markup


async def district_markup(region_id):
    async with aiofiles.open("/home/dilshod/PycharmProjects/Python_21/module_5/lesson_2/buttons/district.json","rb") as f:
        data = (await f.read())
        districts = json.loads(data)
    buttons = []
    for district in districts:
        if district.get("region_id") == region_id:
            btn = InlineKeyboardButton(text=district.get("name_uz"), callback_data="district_" + district.get("id"))
            buttons.append(btn)
    markup = InlineKeyboardBuilder()
    markup.add(*buttons)
    markup.adjust(2, repeat=True)
    markup = markup.as_markup()
    return markup


async def menu_button():
    btn1 = KeyboardButton(text="Kompaniya1 haqida")
    btn2 = KeyboardButton(text="Phone Number ☎️", request_contact=True)
    btn3 = KeyboardButton(text="Location 📍", request_location=True)
    btn4 = KeyboardButton(text="Kompaniya4 haqida")
    btn5 = KeyboardButton(text="Kompaniya5 haqida")
    btn6 = KeyboardButton(text="Kompaniya6 haqida")
    btn7 = KeyboardButton(text="Kompaniya7 haqida")
    markup = ReplyKeyboardBuilder()
    markup.add(*[btn1, btn2, btn3, btn4, btn5, btn6, btn7])
    markup.adjust(2, 1, 2, 2)
    markup = markup.as_markup()
    return markup


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", parse_mode=ParseMode.HTML)


@dp.message(Command('region'))  # message.text == "/region"
async def region_message_handler(message: Message):
    await message.answer("Viloyatlar jadvali", reply_markup=(await region_markup()))


@dp.callback_query(F.data.startswith('region_'))
async def region_id_handler(callback: CallbackQuery):
    region_id = callback.data.split("_")[1]
    markup = await district_markup(region_id)
    await callback.message.edit_text("Tumanlar", reply_markup=markup)


@dp.message(Command("evos"))
async def evos_handler(message: Message):
    menu = await menu_button()
    await message.answer_photo("https://telegra.ph/file/a7f782058a534406d9205.png", reply_markup=menu)


# @dp.message(F.photo)
# async def photo_handler(message : Message):
#     file = await message.bot.get_file(message.photo[-1].file_id)
#     download_file = await message.bot.download_file(file.file_path)
# response = requests.post('https://telegra.ph/upload', files={'file': download_file})
# with open("ixtiyoriy.png" , 'wb') as f:
#     f.write(download_file.read())
# data = response.json()
# url = "https://telegra.ph" + data[0].get('src').replace(r"\\", '')
# print(url)


async def main() -> None:
    P = "http://proxy.server:3128"
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
