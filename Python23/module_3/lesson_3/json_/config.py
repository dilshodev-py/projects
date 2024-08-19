import json


class File:
    def read(self):
        file_name = self.__class__.__name__.lower() + "s.json"
        with open(file_name, 'r') as f:
            data = json.load(f)
        for i, v in enumerate(data):
            data[i] = self.__class__(**v)
        return data

    def write(self, data: list):
        file_name = self.__class__.__name__.lower() + "s.json"
        for i, v in enumerate(data):
            data[i] = v.__dict__
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=3)


class User(File):
    def __init__(self, id=None, name=None, age=None):
        self.id = id
        self.name = name
        self.age = age

    def sequence_id(self):
        users: list[User] = self.read()
        return users[-1].id + 1 if users else 1

    def save(self):
        data: list[dict] = self.read()
        data.append(self.__dict__)
        self.write(data)
