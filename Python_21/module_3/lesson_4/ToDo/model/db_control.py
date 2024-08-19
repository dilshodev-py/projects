import json
import aiofiles
from module_3.lesson_4.ToDo.config import BASE_PATH
from os.path import join

DB_PATH = join(BASE_PATH, "database")


class File:
    @classmethod
    async def all(cls) -> list:
        file_name = cls.__name__.lower() + "s.json"
        async with aiofiles.open(join(DB_PATH, file_name), 'r') as f:
            data = await f.read()
            data = json.loads(data)

        for i, dict_ in enumerate(data):
            data[i] = cls(**dict_)
        return data

    @classmethod
    async def write(cls, data: list) -> None:
        file_name = cls.__name__.lower() + "s.json"
        for i, obj in enumerate(data):
            data[i] = obj.__dict__
        async with aiofiles.open(join(DB_PATH, file_name), 'w') as f:
            data = json.dumps(data, indent=3)
            await f.write(data)

# project + async - database

# telegram Bot  + async
#               - database

# Django
# FastApi -> async








#
# user = User(1 , "Botir" , 'botir@gmail.com' , '1111' , '2024-02-22')
#
# print(User().write([user , user]))
# print(User().all())
