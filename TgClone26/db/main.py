import json
from os.path import join
from utils import BASE_PATH

DB_PATH = join(BASE_PATH, 'db' , 'database')


class DB:
    @property
    def objects(self):
        file_name = self.__class__.__name__.lower() + "s.json"
        with open(join(DB_PATH, file_name), 'r') as f:
            data = json.load(f)
        res = []
        for i in data:
            res.append(self.__class__(**i)) # noqa
        return res

    def write(self, data: list[objects]):
        file_name = self.__class__.__name__.lower() + "s.json"
        res = []
        for i in data:
            res.append(i.__dict__)
        with open(join(DB_PATH, file_name), 'w') as f:
            json.dump(res, f, indent=3)
