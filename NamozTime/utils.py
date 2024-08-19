import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup
import httpx

async def get_temp():
    async with httpx.AsyncClient() as r:
        temp =  await r.get("https://namozvaqti.uz/shahar/toshkent")
    return temp.content


async def parse_time():
    temp_code = await get_temp()
    soup = BeautifulSoup(temp_code , "html.parser")
    rows = soup.find("div", "ad__in")
    result = []
    for row in rows.find_all("p" , "time"):
        result.append({"name" : row["id"], "time" : row.text})
    return result


def button(data) :
    design = []
    for i in range(2):
        row = []
        for i in data[i*3:i*3+3]:
            row.append(KeyboardButton(text = i[0].name))
        design.append(row)
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
