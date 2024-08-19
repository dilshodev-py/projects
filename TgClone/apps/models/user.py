from dataclasses import dataclass

from apps.errors import UserException
from apps.language.lang import data
from apps.models.utils import DB
from apps.utils.settings import Settings


@dataclass
class User(DB):
    id : int = None
    fullname : str = None
    phone_number : str = None
    username : str = None
    email : str = None
    photo : str = None
    lang : str = None
    bio : str = None

    async def save_user(self):
        users : list[User] = await self.get_data()
        users.append(self)
        await self.save(users)

    async def sequence_id(self):
        users : list[User] = await self.get_data()
        return users[-1].id + 1 if users else 1

    async def is_unique_phone_number(self):
        users : list[User] = await self.get_data()
        for user in users:
            if user.phone_number == self.phone_number:
                return False
        return True

    async def is_unique_username(self):
        users : list[User] = await self.get_data()
        for user in users:
            if user.username == self.username:
                return False
        return True

    async def is_valid(self):
        users_errors = data.get(self.lang).get('users').get('errors')
        if len(self.phone_number) != 13:
            raise UserException(users_errors.get('check_phone_number'))
        if not (await self.is_unique_phone_number()):
            raise UserException(users_errors.get('is_unique_phone_number'))
        if not (await self.is_unique_username()):
            raise UserException(users_errors.get('is_unique_username'))

    async def is_auth(self):
        users : list[User] = await self.get_data()
        for user in  users:
            if user.phone_number == self.phone_number:
                users_errors = data.get(user.lang).get('users').get('errors')
                code = await Settings.email.send_email_code(user.email)
                user_code = input("Send code to email : ")
                if str(code) != user_code:
                    raise UserException(users_errors.get('wrong_code'))
                return user
        raise UserException(data.get('uz').get('users').get('errors').get('not_found_user'))



















