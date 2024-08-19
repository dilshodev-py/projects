from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
import pandas as pd

API_ID = 20219166

API_HASH = '0b023d8fb22abf1b5ee1db73be13373d'
phone_number = '+998981214545'

client = TelegramClient(f'session_{phone_number}', API_ID, API_HASH)


def from_specific_user(event):
    return event.text == 'send'

@client.on(events.NewMessage(func=from_specific_user))
async def main(event):
    data = pd.read_excel('error_send.xlsx')
    # for i in data.values:
        # if i[0][1:].isdigit():
        #     PHONE_NUMBER = "+" + str(i[0])
        #     MESSAGE = i[1]
        #     FIRST_NAME = i[2]
        #     contact = InputPhoneContact(
        #         client_id=0,
        #         phone=PHONE_NUMBER,
        #         first_name=FIRST_NAME,
        #         last_name=' '
        #     )
        #     result = await client(ImportContactsRequest([contact]))
        #     if not result.users:
        #         raise Exception("Not Found account")
        #     print(result.stringify())
        # else:
        #     PHONE_NUMBER = i[0]
    chat_id = await client.get_entity('1234543')
    await client.send_message(chat_id.id, 'salom shuhrat aka')

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
