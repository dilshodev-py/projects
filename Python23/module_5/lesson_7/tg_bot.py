import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

TOKEN = "7008756551:AAHuQwCQAzTem9TzrvS-hi_ljudYp68MSTk"

dp = Dispatcher()

books = [
    {
        "id": 1,
        "name": "Oq Kema",
        "photo": 'https://telegra.ph/file/aaa3ca912bae762e1b03a.png',
        "price": 50000
    },
    {
        "id": 2,
        "name": "Pycharm",
        "photo": 'https://telegra.ph/file/feab6d06b25dc6231e686.png',
        "price": 1000000
    }
]


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    design = [
        [
            InlineKeyboardButton(text='Search 🔎', switch_inline_query_current_chat='')
        ]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=ikm)


@dp.inline_query()
async def inline_query_handler(query: InlineQuery) -> None:
    book_s = []
    filter = []
    for b in books:
        if query.query.lower() in b.get('name').lower():
            filter.append(b)

    for book in filter:
        book_s.append(InlineQueryResultArticle(
            id=str(book.get("id")),
            title=book.get("name"),
            thumbnail_url=book.get("photo"),
            description=f"Price :{book.get('price')}",
            input_message_content=InputTextMessageContent(message_text=book.get('name'))
        ))
    await query.answer(book_s)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
