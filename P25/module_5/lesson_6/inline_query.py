import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

TOKEN = "7478312427:AAEkiYYGSIp-KvvEtSP3nUj04K1s2EH-dx0"

dp = Dispatcher()

@dp.inline_query()
async def books_list(inline : InlineQuery):
    result = [
        InlineQueryResultArticle(
            id=str(1),
            title="Oq Kema",
            description=str(f"P25 books\n💴 Narxi: 45000 so'm"),
            thumbnail_url="https://telegra.ph/file/aaa3ca912bae762e1b03a.png",
            input_message_content=InputTextMessageContent(message_text="1")
        )
        ]
    await inline.answer(result, cache_time=5, is_personal=True)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())