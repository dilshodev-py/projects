import asyncio
import logging
import os

import aiofiles
import instaloader
from aiogram import Router, F
from aiogram.enums import ChatMemberStatus, ChatAction
from aiogram.types import Message, InputFile, FSInputFile, BufferedInputFile
from instaloader import Post
from pip._internal.exceptions import NetworkConnectionError

from bot.buttons.inlines import referral_btn
from db.models.insta import Insta

from db.models.users import Referal
import subprocess
insta_router = Router()
loader = instaloader.Instaloader()
USERNAME = "dilshod_ev"
PASSWORD = "Qwer123**"
try:
    loader.login(USERNAME, PASSWORD)
except:
    two_factor_code = input("Enter 2FA code: ")
    loader.context.two_factor_login(two_factor_code)
DOWNLOAD_DIR = 'downloads/'

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# def compress_video(input_file, output_file):
#     command = [
#         'ffmpeg', '-i', input_file,
#         '-vf', 'scale=1280:-1',  # Resize to width 1280, keeping aspect ratio
#         '-b:v', '1M',            # Set video bitrate to 1M (adjust as needed)
#         '-c:a', 'aac', '-b:a', '128k',  # Set audio codec and bitrate
#         output_file
#     ]
#     subprocess.run(command, check=True)



@insta_router.message(F.text.startswith('https://www.instagram.com/'))
async def command_start_handler(message: Message) -> None:
    referrals = await Referal.get_all()
    l = []
    for i, referral in enumerate(referrals):
        chat = await message.bot.get_chat("@" + referral.link)
        chat_member = await message.bot.get_chat_member(chat.id, message.from_user.id,request_timeout=1)
        if chat_member.status == ChatMemberStatus.LEFT:
            l.append(referral)
    if l:
        await message.answer("Quydagi kannal guruhlarga azo bo'ling",
                             reply_markup=(await referral_btn(l)))

    else:
        post_url = message.text
        shortcode = post_url.split("/")[-2]
        r = await Insta.get_by_shortcode(shortcode = shortcode)
        if r:
            await message.answer_video(video=r.file_id)
            await message.answer(text="Here's your Instagram video!")

        else:
            # video_path = '/home/dilshod/PycharmProjects/InstagramDownloadBot/PSKENTDA_POYGA_CHEMPION_YONIB_KETDI_DRAG_RACING_2023.webm'
            # compressed_file = 'compressed_video.mp4'
            # compress_video(video_path, compressed_file)

            # with open(compressed_file, 'rb') as video:
            #     video = BufferedInputFile(video.read(), 'h.mp4')
            #     await message.bot.send_video(message.chat.id, video, caption="Here's your compressed video!")

            await message.answer('⏳')
            await message.bot.send_chat_action(message.chat.id, action=ChatAction.UPLOAD_VIDEO)
            post = Post.from_shortcode(loader.context, shortcode)
            if post.is_video:
                if post.video_duration < 50:
                    video_url = post.video_url
                    await message.bot.delete_message(message.chat.id, message.message_id + 1)
                    m = await message.answer_video(video=video_url)
                    await Insta.create(file_id = m.video.file_id , shortcode=shortcode)
                    await message.answer(text="Here's your Instagram video!")
                else:
                    await message.answer(text=post.video_url)







