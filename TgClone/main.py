import asyncio
from typing import Optional
from colorama import Fore
from apps.errors import UserException
from apps.models.user import User
from apps.utils.settings import Settings

settings = Settings()
session_user: Optional[User] = None


class UI:
    async def main(self):
        try:
            menu = Fore.GREEN + """
                1) Register
                2) Login
                3) exit
                >>>"""
            match input(menu):
                case "1":
                    await self.register()
                case "2":
                    await self.login()
                case "3":
                    return
        except UserException as m:
            print(Fore.RED + str(m))
            await self.main()

    async def register(self):

        form_account = {
            "id": (await User().sequence_id()),
            "fullname": input(Fore.BLUE + 'fullname: '),
            "phone_number": input(Fore.BLUE + 'phone_number: '),
            "username": input(Fore.BLUE + 'username: '),
            "email": input(Fore.BLUE + 'email: '),
            "photo": (await settings.sticker.user()),
            "lang": (await settings.lang.choose_lang()),
            "bio": input(Fore.BLUE + 'bio: ')
        }
        user = User(**form_account)
        await user.is_valid()
        await user.save_user()
        await self.main()

    async def login(self):
        global session_user
        auth = {
            'phone_number': input(Fore.BLUE + 'Phone number : ')
        }
        auth = User(**auth)
        session_user = await auth.is_auth()
        await self.account()

    async def account(self):
        print(Fore.YELLOW + "-------------- Welcome -----------------")


asyncio.run(UI().main())

# moshina ustasi -> shogirt
# unverstet      -> nazariy
