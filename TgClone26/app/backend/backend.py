import random
from abc import ABC, abstractmethod
from datetime import datetime
from os.path import join
from typing import Optional

from pydantic import BaseModel, field_validator

from app.backend.enum_class import Lang
from app.backend.errors import UserError
from app.language.lang import lang_data
from db.main import DB
from utils import BASE_PATH





class CRUD(DB):
    def save(self):
        objects = self.objects
        self.id = objects[-1].id + 1 if objects else 1
        objects.append(self)
        self.write(objects)

    def update(self, **fields):
        objects = self.objects
        for obj in objects:
            if obj.id == self.id:
                for k, v in fields.items():
                    setattr(obj, k, v)
                self.write(objects)
                return obj



    def delete(self):
        objects = self.objects
        for obj in objects:
            if obj.id == self.id:
                objects.remove(obj)
                self.write(objects)
                break

    def read(self):
        objects = self.objects
        for obj in objects:
            if obj.id == self.id:
                return obj


class User(BaseModel, CRUD):
    id: int = None
    first_name: str = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    image: Optional[str] = None
    phone_number: str = None
    bio: Optional[str] = None
    birthdate: Optional[str] = None
    lang: str = Lang.en.name
    created_at: str = None


    @field_validator('phone_number')  # noqa
    @classmethod
    def phone_number_validator(cls, v):
        data = lang_data['en']
        if len(v) != 12:
            raise UserError(data['phone_number_invalid_message'])
        return v

    @field_validator('birthdate')  # noqa
    @classmethod
    def birthdate_validator(cls, v):
        if v is None:
            return v
        try:
            datetime.fromisoformat(v)
        except ValueError as e:
            raise UserError(e)
        return v

    def user_objects(self , users_id : set[int]):
        users : list[User] = self.objects
        for user in users:
            if user.id in users_id:
                yield user



    def is_auth(self, session_lang=Lang.en.name):
        data = lang_data.get(session_lang)

        users: list[User] = self.objects
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.send_code()
                assert code == input("code"), data.get('invalid_code')
                return user
        else:
            raise UserError(data.get('not_phone_number'))

    def is_unique(self, session_lang=Lang.en.name, username=False, phone_number=False):
        data = lang_data.get(session_lang)
        users: list[User] = self.objects
        for user in users:
            if username:
                if user.username == self.username:
                    raise UserError(data.get('username_unique_message'))
            elif phone_number:
                if user.phone_number == self.phone_number:
                    raise UserError(data.get('phone_number_unique_message'))

    def send_code(self):  # noqa
        code = str(random.randrange(10 ** 5, 10 ** 6))
        with open(join(BASE_PATH, 'code.txt'), 'w') as f:
            f.write(code)
        return code


class Chat(BaseModel, CRUD):
    id : int = None
    message : str = None
    type : str = 'user_chat'
    receiver_id : int = None
    sender_id : int = None
    is_seen : bool = False
    send_at : str = str(datetime.now())


    def chat_messages(self):
        chats = self.objects
        for chat in chats:
            if chat.type == self.type:
                if chat.receiver_id == self.receiver_id and chat.sender_id == self.sender_id:
                    yield chat
                elif chat.receiver_id == self.sender_id and chat.sender_id == self.receiver_id:
                    yield chat
    def self_chat_list(self):
        chats : list[Chat]= self.objects
        users_id = set()
        for chat in chats:
            if chat.type == self.type:
                if chat.sender_id == self.sender_id:
                    users_id.add(chat.receiver_id)
                elif chat.receiver_id == self.sender_id:
                    users_id.add(chat.sender_id)

        return User().user_objects(users_id)












