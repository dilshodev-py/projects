"""
OOP tamoillari:
    class

    object

    inheritance

    encapsulation

    polymorphism

    abstraction

try:

except

else

finnaly

file mode:
    r
    w
    x
    a

open()

ProductError()



decorator methods:
    staticmethod
    property
    classmethod
    abstractmethod
    dataclass
    setter



https://dummyjson.com/todos
CRUD classini qurish kerak
data olish kere va json filega yozadigan qilish kere


Time : 19:40
"""
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from os.path import join
from pathlib import Path

# todos = [
#     {
#       "id": 1,
#       "todo": "Do something nice for someone you care about",
#       "completed": False,
#       "userId": 152
#     },
#     {
#       "id": 2,
#       "todo": "Memorize a poem",
#       "completed": True,
#       "userId": 13
#     },
#     {
#       "id": 3,
#       "todo": "Watch a classic movie",
#       "completed": True,
#       "userId": 68
#     },
#     {
#       "id": 4,
#       "todo": "Watch a documentary",
#       "completed": False,
#       "userId": 84
#     },
#     {
#       "id": 5,
#       "todo": "Invest in cryptocurrency",
#       "completed": False,
#       "userId": 163
#     },
#     {
#       "id": 6,
#       "todo": "Contribute code or a monetary donation to an open-source software project",
#       "completed": False,
#       "userId": 69
#     },
#     {
#       "id": 7,
#       "todo": "Solve a Rubik's cube",
#       "completed": True,
#       "userId": 76
#     },
#     {
#       "id": 8,
#       "todo": "Bake pastries for yourself and neighbor",
#       "completed": True,
#       "userId": 198
#     },
#     {
#       "id": 9,
#       "todo": "Go see a Broadway production",
#       "completed": False,
#       "userId": 7
#     },
#     {
#       "id": 10,
#       "todo": "Write a thank you letter to an influential person in your life",
#       "completed": True,
#       "userId": 9
#     },
#     {
#       "id": 11,
#       "todo": "Invite some friends over for a game night",
#       "completed": False,
#       "userId": 104
#     },
#     {
#       "id": 12,
#       "todo": "Have a football scrimmage with some friends",
#       "completed": False,
#       "userId": 32
#     },
#     {
#       "id": 13,
#       "todo": "Text a friend you haven't talked to in a long time",
#       "completed": True,
#       "userId": 2
#     },
#     {
#       "id": 14,
#       "todo": "Organize pantry",
#       "completed": False,
#       "userId": 46
#     },
#     {
#       "id": 15,
#       "todo": "Buy a new house decoration",
#       "completed": True,
#       "userId": 105
#     },
#     {
#       "id": 16,
#       "todo": "Plan a vacation you've always wanted to take",
#       "completed": True,
#       "userId": 162
#     },
#     {
#       "id": 17,
#       "todo": "Clean out car",
#       "completed": False,
#       "userId": 71
#     },
#     {
#       "id": 18,
#       "todo": "Draw and color a Mandala",
#       "completed": True,
#       "userId": 6
#     },
#     {
#       "id": 19,
#       "todo": "Create a cookbook with favorite recipes",
#       "completed": True,
#       "userId": 53
#     },
#     {
#       "id": 20,
#       "todo": "Bake a pie with some friends",
#       "completed": False,
#       "userId": 162
#     },
#     {
#       "id": 21,
#       "todo": "Create a compost pile",
#       "completed": False,
#       "userId": 13
#     },
#     {
#       "id": 22,
#       "todo": "Take a hike at a local park",
#       "completed": True,
#       "userId": 37
#     },
#     {
#       "id": 23,
#       "todo": "Take a class at local community center that interests you",
#       "completed": True,
#       "userId": 65
#     },
#     {
#       "id": 24,
#       "todo": "Research a topic interested in",
#       "completed": True,
#       "userId": 130
#     },
#     {
#       "id": 25,
#       "todo": "Plan a trip to another country",
#       "completed": False,
#       "userId": 140
#     },
#     {
#       "id": 26,
#       "todo": "Improve touch typing",
#       "completed": False,
#       "userId": 178
#     },
#     {
#       "id": 27,
#       "todo": "Learn Express.js",
#       "completed": False,
#       "userId": 194
#     },
#     {
#       "id": 28,
#       "todo": "Learn calligraphy",
#       "completed": False,
#       "userId": 80
#     },
#     {
#       "id": 29,
#       "todo": "Have a photo session with some friends",
#       "completed": True,
#       "userId": 91
#     },
#     {
#       "id": 30,
#       "todo": "Go to the gym",
#       "completed": True,
#       "userId": 142
#     }
#   ]

# for todo in todos:
#     Todo(**todo).create()

# Todo(id = 1 , todo = "Nimadir",completed=True , userId = 10).create()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = join(BASE_DIR, 'db')

todos = [
    {
        "id": 1,
        "todo": "Do something nice for someone you care about",
        "completed": False,
        "userId": 152
    },
    {
        "id": 2,
        "todo": "Memorize a poem",
        "completed": True,
        "userId": 13
    },
    {
        "id": 3,
        "todo": "Watch a classic movie",
        "completed": True,
        "userId": 68
    },
    {
        "id": 4,
        "todo": "Watch a documentary",
        "completed": False,
        "userId": 84
    },
    {
        "id": 5,
        "todo": "Invest in cryptocurrency",
        "completed": False,
        "userId": 163
    },
    {
        "id": 6,
        "todo": "Contribute code or a monetary donation to an open-source software project",
        "completed": False,
        "userId": 69
    },
    {
        "id": 7,
        "todo": "Solve a Rubik's cube",
        "completed": True,
        "userId": 76
    },
    {
        "id": 8,
        "todo": "Bake pastries for yourself and neighbor",
        "completed": True,
        "userId": 198
    },
    {
        "id": 9,
        "todo": "Go see a Broadway production",
        "completed": False,
        "userId": 7
    },
    {
        "id": 10,
        "todo": "Write a thank you letter to an influential person in your life",
        "completed": True,
        "userId": 9
    },
    {
        "id": 11,
        "todo": "Invite some friends over for a game night",
        "completed": False,
        "userId": 104
    },
    {
        "id": 12,
        "todo": "Have a football scrimmage with some friends",
        "completed": False,
        "userId": 32
    },
    {
        "id": 13,
        "todo": "Text a friend you haven't talked to in a long time",
        "completed": True,
        "userId": 2
    },
    {
        "id": 14,
        "todo": "Organize pantry",
        "completed": False,
        "userId": 46
    },
    {
        "id": 15,
        "todo": "Buy a new house decoration",
        "completed": True,
        "userId": 105
    },
    {
        "id": 16,
        "todo": "Plan a vacation you've always wanted to take",
        "completed": True,
        "userId": 162
    },
    {
        "id": 17,
        "todo": "Clean out car",
        "completed": False,
        "userId": 71
    },
    {
        "id": 18,
        "todo": "Draw and color a Mandala",
        "completed": True,
        "userId": 6
    },
    {
        "id": 19,
        "todo": "Create a cookbook with favorite recipes",
        "completed": True,
        "userId": 53
    },
    {
        "id": 20,
        "todo": "Bake a pie with some friends",
        "completed": False,
        "userId": 162
    },
    {
        "id": 21,
        "todo": "Create a compost pile",
        "completed": False,
        "userId": 13
    },
    {
        "id": 22,
        "todo": "Take a hike at a local park",
        "completed": True,
        "userId": 37
    },
    {
        "id": 23,
        "todo": "Take a class at local community center that interests you",
        "completed": True,
        "userId": 65
    },
    {
        "id": 24,
        "todo": "Research a topic interested in",
        "completed": True,
        "userId": 130
    },
    {
        "id": 25,
        "todo": "Plan a trip to another country",
        "completed": False,
        "userId": 140
    },
    {
        "id": 26,
        "todo": "Improve touch typing",
        "completed": False,
        "userId": 178
    },
    {
        "id": 27,
        "todo": "Learn Express.js",
        "completed": False,
        "userId": 194
    },
    {
        "id": 28,
        "todo": "Learn calligraphy",
        "completed": False,
        "userId": 80
    },
    {
        "id": 29,
        "todo": "Have a photo session with some friends",
        "completed": True,
        "userId": 91
    },
    {
        "id": 30,
        "todo": "Go to the gym",
        "completed": True,
        "userId": 142
    }
]


class DbManager:
    @property
    def objects(self):
        file_name = self.__class__.__name__.lower() + "s.json"
        with open(join(DB_PATH, file_name), 'r') as f:
            data = json.load(f)
        for i, d in enumerate(data):
            data[i] = self.__class__(**d)  # noqa
        return data

    def write(self, data: list[objects]):
        file_name = self.__class__.__name__.lower() + "s.json"
        res = [i.__dict__ for i in data]
        with open(join(DB_PATH, file_name), 'w') as f:
            json.dump(res, f, indent=3)


class CRUD(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def read(self):
        pass


@dataclass
class Todo(DbManager, CRUD):
    id: int = None
    todo: str = None
    completed: bool = None
    userId: int = None

    def create(self):
        todos = self.objects
        todos.append(self)
        self.write(todos)

    def update(self, **fields):
        todos = self.objects
        for todo in todos:
            if todo.id == self.id:
                for k , v in fields.items():
                    setattr(todo, k, v)
                self.write(todos)
                break

    def delete(self):
        todos = self.objects
        for todo in todos:
            if todo.id == self.id:
                todos.remove(todo)
                self.write(todos)
                break

    def read(self):
        todos = self.objects
        for todo in todos:
            if todo.id == self.id:
                return todo



