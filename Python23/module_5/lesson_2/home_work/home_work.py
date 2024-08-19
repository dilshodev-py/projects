import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from module_5.lesson_2.home_work.ORM import Member, Document

TOKEN = "7008756551:AAEQwgy8tRidl-EsOnZzAbk_704f9ekBzSA"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    user: list[tuple] = Member().select(user_id = message.from_user.id)
    if not user:
        Member(user_id=message.from_user.id ,
               first_name=message.from_user.first_name ,
               last_name=message.from_user.last_name ,
               username=message.from_user.username).insert()
    file_id = Document().select(id = 1)[0][2]
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer_document(document=file_id)


@dp.message((F.photo) | (F.document) | (F.video))
async def save_file_doc_video(message : Message):
    if message.photo:
        Document(owner_id=message.from_user.id , file_id=message.photo[0].file_id , type='photo').insert()
    elif message.video:
        Document(owner_id=message.from_user.id , file_id=message.video.file_id, type = 'video').insert()
    elif message.document:
        Document(owner_id=message.from_user.id , file_id=message.document.file_id , type='document').insert()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())