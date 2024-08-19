from dataclasses import dataclass
from os.path import join
from pathlib import Path

DB_PATH = Path(__file__).parent


class DbService:
    def objects(self) -> list:
        file_name = self.__class__.__name__.lower() + 's.txt'
        with open(join(DB_PATH , file_name) , 'r') as f:
            data = f.readlines()
        for i , value in enumerate(data):
            data[i] = self.__class__(*list(map( lambda x : x.strip(), value.split(','))))
        return data

    def write(self, data: list) -> None:
        file_name = self.__class__.__name__.lower() + 's.txt'
        tmp = ""
        for obj in data:
            tmp += ",".join(map(str , obj.__dict__.values())) + "\n"
        with open(join(DB_PATH , file_name) , 'w') as f:
            f.write(tmp)






