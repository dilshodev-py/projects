import random

from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact, InputUser, InputUserEmpty, InputUserSelf
import pandas as pd
import asyncio

API_ID = 20219166
API_HASH = '0b023d8fb22abf1b5ee1db73be13373d'
phone_number = '+998993583234'

client = TelegramClient(f'session_{phone_number}', API_ID, API_HASH)


def from_specific_user(event):
    return event.text == 'send'
# C:/Users/User/Desktop/error_send.xlsx

@client.on(events.NewMessage(func=from_specific_user))
async def main(event):
    data = pd.read_excel('error_send.xlsx')
    face_phone_number = []
    c = 0
    for i in data.values:
        c += 1
        phone_n = str(i[0])
        try:
            if phone_n[1:].isdigit():
                PHONE_NUMBER = "+" + phone_n
                MESSAGE = i[1]
                FIRST_NAME = i[2]
                contact = InputPhoneContact(client_id=0,phone=PHONE_NUMBER,first_name=FIRST_NAME,last_name=' ')
                result = await client(ImportContactsRequest([contact]))
                if not result.users:
                    face_phone_number.append(str(i[0]))
                    continue
                print(result.stringify())
            else:
                MESSAGE = i[1]
                PHONE_NUMBER = i[0]
            user = await client.get_entity(PHONE_NUMBER)
            await client.send_message(user.id, MESSAGE)
            await client(DeleteContactsRequest(id=[user.id]))
        except:
            print(f"Xatolik : {i[0]}")
            face_phone_number.append(str(i[0]))
        await asyncio.sleep(random.randrange(4, 10))

        if c >= 30:
            with open('egg.xlsx', 'a') as f:
                f.write("\n"+"\n".join(face_phone_number))
                face_phone_number = []




# MESSAGE = i[1]
# PHONE_NUMBER = i[0]
# contact = InputPhoneContact(client_id=0, phone=PHONE_NUMBER, first_name=' ', last_name=' ')
# user = ImportContactsRequest([contact]).contacts[0]
# await client.send_message(user.client_id, MESSAGE)
# await client(DeleteContactsRequest(id=[user.client_id]))
if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()

