from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
import pandas as pd
import asyncio

API_ID = 20219166
API_HASH = '0b023d8fb22abf1b5ee1db73be13373d'
phone_number = '+998981214545'

client = TelegramClient(f'session_{phone_number}', API_ID, API_HASH)


def from_specific_user(event):
    return event.text == 'send'
# C:/Users/User/Desktop/eggg.xlsx

@client.on(events.NewMessage(func=from_specific_user))
async def main(event):
    data = pd.read_excel('C:/Users/User/Desktop/eggg.xlsx')
    face_phone_number = []

    for i in data.values:
        phone_n = str(i[0])
        try:
            if phone_n[1:].isdigit():
                PHONE_NUMBER = "+" + phone_n
                MESSAGE = i[1]
                FIRST_NAME = i[2]
                contact = InputPhoneContact(
                    client_id=0,
                    phone=PHONE_NUMBER,
                    first_name=FIRST_NAME,
                    last_name=' '
                )
                result = await client(ImportContactsRequest([contact]))
                if not result.users:
                    face_phone_number.append(str(i[0]))
                    continue
                print(result.stringify())
            else:
                MESSAGE = i[1]
                PHONE_NUMBER = i[0]
            chat_id = await client.get_entity(PHONE_NUMBER)
            await client.send_message(chat_id.id, MESSAGE)
        except:
            print(f"Xatolik : {i[0]}")
            face_phone_number.append(str(i[0]))
        await asyncio.sleep(3)
    with open('C:/Users/User/Desktop/no_send_txt', 'w') as f:
        f.write("\n".join(face_phone_number))

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()