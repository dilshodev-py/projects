# aiofiles
# httpx
# bs4
import json
from os.path import join

import aiofiles as aiofiles

from apps.utils.settings import BASE_URL

DB_URL = join(BASE_URL, 'apps', 'database')


class DB:

    async def get_data(self):
        filename = self.__class__.__name__.lower() + "s.json"
        try:
            async with aiofiles.open(join(DB_URL, filename), 'r') as f:
                data = json.loads((await f.read()))
            for i, v in enumerate(data):
                data[i] = self.__class__(**v)
        except:
            data = []
        return data

    async def save(self, data: list[object]):
        filename = self.__class__.__name__.lower() + "s.json"

        for i, v in enumerate(data):
            data[i] = v.__dict__

        async with aiofiles.open(join(DB_URL, filename), 'w') as f:
            json_data: str = json.dumps(data, indent=3)
            await f.write(json_data)
