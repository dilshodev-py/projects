import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand, InlineKeyboardButton, CallbackQuery, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from module_5.lesson_6.tasks import send_email

TOKEN = "7478312427:AAEkiYYGSIp-KvvEtSP3nUj04K1s2EH-dx0"

dp = Dispatcher()

def reply_net_link():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text = "Instagram" , web_app=WebAppInfo(url="https://www.instagram.com")),
        KeyboardButton(text = "Kun uz" , web_app=WebAppInfo(url="https://kun.uz")),
        # KeyboardButton(text = "Telegram Me" , web_app=WebAppInfo(url="https://t.me/dilshod_absaitov")),
    ])
    rkb.adjust(2,1)
    return rkb.as_markup(resize_keyboard=True)

def inline_net_link():
    rkb = InlineKeyboardBuilder()
    rkb.add(*[
        InlineKeyboardButton(text = "Instagram" , url="https://www.instagram.com"),
        InlineKeyboardButton(text = "Kun uz" , url="https://kun.uz"),
        InlineKeyboardButton(text = "Telegram Me" , url="https://t.me/dilshod_absaitov"),
    ])
    rkb.adjust(2,1)
    return rkb.as_markup()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.bot.set_my_commands([
        BotCommand(command='/start' , description="Qaytadan ishga tushurish" ),
        BotCommand(command='/pagination' , description="pagination ishga tushurish" ),
    ])
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!" , reply_markup=inline_net_link())
    await message.answer(f"Link Evos {html.link('evos' , 'https://evos.uz')}")

def inline_menu(page_num : int = 0):
    ikb = InlineKeyboardBuilder()
    ikb.add(*[
        InlineKeyboardButton(text = "<-" , callback_data=f'page_num_{page_num - 1}'),
        InlineKeyboardButton(text = f"{page_num}" , callback_data='current_page}'),
        InlineKeyboardButton(text="->", callback_data=f'page_num_{page_num + 1}'),
    ])
    ikb.adjust(3)
    return ikb.as_markup()


class EmailState(StatesGroup):
    email = State()
@dp.message(Command("email"))
async def send_command_handler(message : Message , state : FSMContext):
    await state.set_state(EmailState.email)
    await message.answer("Enter your email !")

@dp.message(EmailState.email)
async def email_handelr(message : Message , state : FSMContext):
    if "@" in message.text:
        send_email.delay(message.text)
        await message.answer("Emailga habar yuborildi")
    else:
        await message.answer("Emailda hatolik bor")


@dp.message(Command("pagination"))
async def pag_handler(message : Message , state :FSMContext):
    await message.answer(text = "Pagination" , reply_markup=inline_menu(0))

@dp.callback_query(F.data.startswith('page_num_'))
async def pag_handler(call : CallbackQuery):
    page_num = int(call.data.split('_')[-1])
    if page_num < 0:
        await call.answer("Manfiy page ga o'tib bo'lmaydi")
    else:
        await call.message.edit_reply_markup(reply_markup=inline_menu(page_num))




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())