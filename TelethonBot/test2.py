from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

API_ID = 24674072
API_HASH = 'd97364c2c93786e23332ee0825865bcd'
phone_number = '+998993583234'

client = TelegramClient(f'session_{phone_number}', API_ID, API_HASH)

def from_specific_user(event):
    return event.text == 'go'

@client.on(events.NewMessage(func=from_specific_user))
async def main(event):
    contact = InputPhoneContact(
        client_id=0,
        phone='+998906179980',
        first_name='b',
        last_name='a'
    )
    result = await client(ImportContactsRequest([contact]))
    print(result.stringify())
    chat_id = await client.get_entity('+998906179980')
    await client.send_message(chat_id.id, 'Hello to myself!')


