from pathlib import Path
from os.path import join

BASE_DIR = Path(__file__).parent.parent
DB_PATH = join(BASE_DIR, 'db', 'database')


class DB:

    @property
    def objects(self) -> list:
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(join(DB_PATH, file_name), 'r') as f:
            readlines = f.readlines()

        res = []
        for data in readlines:
            res.append(self.__class__.from_str(data))
        return res

    def write(self, data: list):
        file_name = self.__class__.__name__.lower() + "s.txt"
        data = "\n".join(["|".join(map(str, i.__dict__.values())) for i in data])
        with open(join(DB_PATH, file_name), 'w') as f:
            f.write(data)
