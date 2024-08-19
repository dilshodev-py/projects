import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7169306709:AAE9Vydeu8VHBJxFsz3QG9Uq2eGLtOcjucE"
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", parse_mode=ParseMode.HTML)


#
# def is_phone_number(message :Message):
#
#     codes = [33,99,98,90,91,93,94,33,88,97,71,95,77,55,20]
#     phone_number = message.text.replace(" ", '')
#     if not phone_number[1:].isdigit():
#         return False
#     if not phone_number.startswith('+') and phone_number.startswith('998'):
#         phone_number = "+"+phone_number
#     if not phone_number.startswith('+998'):
#         phone_number = "+998"+phone_number
#
#     return len(phone_number) == 13 and int(phone_number[4:6]) in codes
#
#
# @dp.message(is_phone_number)
# async def phone_number_handler(message: Message):
#     await message.answer(text = "Valid !")
# @dp.message(F.photo) # magic filter
# async def photo_handler(message: Message):
#     file_id = message.photo[0].file_id
#     await message.reply(text = "Rasm jo'natildi !")
#     await message.answer_photo(photo=file_id ,caption = "Rasm jo'natildi !" )
#     await message.bot.send_photo(chat_id=6199875730 , photo=file_id)
#
# admins = [12,  43 , 54]
# @dp.message(F.from_user.id == 'mybot')
# @dp.message(F.from_user.id.in_(admins))
# @dp.message(Command("mybot"))
# async def my_bot_command_handler(message : Message):
#     await message.reply("mybot command ishladi !")

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# phone_number
#     +99899 123 45 56
#     +99834 123 45 56
#     99834 123 45 56
#     33 123 45 56
#     991234556

# Valid !

# ============== photo save ============
"""psycopg2"""
"""botga yuborilgan rasmlarni file id isini postgresql ga saqlimiz"""

# ============== video save ============
"""botga yuborilgan videolarni file id isini postgresql ga saqlimiz"""

# ============== tarjima bot ============
"""biror bir gap botga yozib jo'natilsa, yuborilgan gapni eng tiliga tarjima qilib bersin """

# ============== Get Me ID ==============
"""botga /start bosgan foydalanuvchilarga id sini qaytaradigan """

# ============== Get File ID ============
"""botga yuborilgan rasmlarni 3 xil file_id larini format qilib (chiroyli qilib) qaytaradigan qilinsin """

# ============== Get Users Count from Group ============
"""Group dan kelgan habardan group_id olib shu id ga tegishli guruhni userlar soni"""

# TODO shu tasklar bajarilmasa o'rnimizdan turamiz !
