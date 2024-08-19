import asyncio
import json
import requests
import aiofiles


data = requests.get("https://65ab6bacfcd1c9dcffc65c27.mockapi.io/ap1/id/product").json()

async def write_json(data):
    data_json = json.dumps(data , indent=3)
    async with aiofiles.open("product.json" , "w") as f:
        await f.write(data_json)

asyncio.run(write_json(data))