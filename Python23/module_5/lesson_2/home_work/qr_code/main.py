import asyncio
import logging
import sys
from os import getenv
import segno

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types import Message, InputFile, FSInputFile, ChatMemberUpdated

from module_5.lesson_2.home_work.ORM import Member, Document

TOKEN = "7008756551:AAEQwgy8tRidl-EsOnZzAbk_704f9ekBzSA"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    print(await message.bot.get_chat_member_count(message.chat.id))
    await message.answer("Assalom , Link yuboring qr code yasab beramiz !")

# @dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
# async def join_member(event: ChatMemberUpdated , bot : Bot):
#     await bot.send_message(chat_id=-1002053684330, text=f"Бот добавлен в {event.chat.title}, username: {event.chat.username}")



# @dp.message(F.text)
# async def message_handler(message : Message):
#     qrcode = segno.make_qr(message.text)
#     url = '/home/dilshod/PycharmProjects/Python23/module_5/lesson_2/home_work/qr_code/photo/'
#     qrcode.save(url + 'qr.png')
#     photo = FSInputFile(url + 'qr.png')
#     await message.answer_photo(photo=photo)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())