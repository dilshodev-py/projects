import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ChatType
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

TOKEN = '7149796467:AAGlZuIrwY6b9dk2pvRKfKetKToDyvPXDq8'  # @npmm_bot
dp = Dispatcher()
books = [
    {
        "id": 1,
        "name": "Ikki dunyo",
        "image": "https://telegra.ph/file/a7d72d0c776605249fe51.png",
        "author": "uzbekistan",
        "price": 150000,
    },
    {
        "id": 2,
        "name": "Oq kema",
        "image": "https://telegra.ph/file/d438ec818cb3dcd460243.png",
        "author": "uzbekistan",
        "price": 100000,
    },
    {
        "id": 3,
        "name": "Pycharm Book",
        "image": "https://telegra.ph/file/feab6d06b25dc6231e686.png",
        "author": "uzbekistan",
        "price": 1000000,
    },
    {
        "id": 4,
        "name": "Docker",
        "image": "https://telegra.ph/file/48a817e55b67756572ed0.png",
        "author": "uzbekistan",
        "price": 1200000,
    }
]


@dp.inline_query()
async def command_start_handler(inline_query: InlineQuery) -> None:
    results = [
        InlineQueryResultArticle(
            id=str(book['id']),
            title=book['name'],
            thumbnail_url=book['image'],
            description=f"{book['author']}\n💴 Narxi: {book['price']} so'm",
            input_message_content=InputTextMessageContent(
                message_text=book['name'],
            )
        )
        for book in books
    ]
    await inline_query.answer(results, cache_time=5, is_personal=True)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())