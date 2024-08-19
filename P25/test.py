import asyncio
import logging
import sys

import requests
from aiogram import Bot, Dispatcher, html, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile, FSInputFile, BufferedInputFile
import instaloader
from instaloader import Post

loader = instaloader.Instaloader()

TOKEN = "6859773237:AAGUZMEbbS9B-RkwbEBOLnEjc1sTmQRuYkM"

USERNAME = "it.master.py"
PASSWORD = "Qwer123*"
loader.login(USERNAME, PASSWORD)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, instagram video linkini yuboring")

@dp.message(F.text.startswith('https://www.instagram.com/'))
async def command_start_handler(message: Message) -> None:
    post_url = message.text
    shortcode = post_url.split("/")[-2]
    await message.answer('⏳')
    await message.bot.send_chat_action(message.chat.id,action=ChatAction.UPLOAD_VIDEO)
    post = Post.from_shortcode(loader.context, shortcode)
    if post.is_video:
        video_url = post.video_url
        response = requests.get(video_url)
        await message.bot.delete_message(message.chat.id,message.message_id + 1)
        await message.reply_video(video=BufferedInputFile(response.content,filename='video.mp4'), caption="Here's your Instagram video!")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
