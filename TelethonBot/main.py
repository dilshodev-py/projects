import asyncio

from telethon import TelegramClient
from telethon import events

API_ID = 24674072
API_HASH = 'd97364c2c93786e23332ee0825865bcd'
phone_number = '+998993583234'

client = TelegramClient(f'session_{phone_number}', API_ID, API_HASH)

# async def main():
#     async with client:
#         if not client.is_user_authorized():
#             await client.send_code_request(phone_number)
#             await client.sign_in(phone_number, input('Enter the code: '))
        # me = await client.get_me()
        # print(me)

@client.on(lambda x :  x.NewMessage == '/send')
async def my_event_handler(event):
    async with client:
        user = await client.get_entity()
        if not user.status:
            await event.reply(f'Absaitov Dilshod hozir javob bera olmaydi!')


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
    # client.loop.run_until_complete(main())

