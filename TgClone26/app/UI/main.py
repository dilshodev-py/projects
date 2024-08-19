import datetime
from typing import Optional
from app.UI.account_ import *
from app.backend.backend import User
from app.backend.enum_class import Lang
from app.backend.errors import UserError
from app.language.lang import lang_data

session_lang = Lang.en.name
session_user: Optional[User] = None


class UI:

    def register(self):
        data = lang_data.get(session_lang)
        user = {
            "phone_number": input(data.get("phone_number"))
        }
        User(**user).is_unique(session_lang, phone_number=True)
        code = User().send_code()
        confirm_code = input(data.get("code"))
        assert code == confirm_code, data.get('invalid_code')
        user.update(
            {
                "first_name": input(data.get("first_name")),
                "last_name": tmp if (tmp := input(data.get("last_name"))) != '' else None,
                "lang": session_lang,
                "created_at": str(datetime.datetime.now()),
            }
        )

        User(**user).save()
        print(data.get('success'))
        self.main()

    def main(self):

        data = lang_data.get(session_lang)
        menu = """
            1) {register}
            2) {login}
            3) {language}
            4) {exit}
            >>>"""
        try:
            match input(menu.format(**data)):
                case '1':
                    self.register()
                case '2':
                    self.login()
                case '3':
                    self.choose_lang()
                case '4':
                    return
        except (UserError, AssertionError) as e:
            print(e)
            self.main()

    def choose_lang(self):
        global session_lang
        for lang in Lang:
            print(f"{lang.value}) {lang.name}")
        select = int(input(">>>"))
        session_lang = Lang(select).name
        self.main()

    def login(self):
        global session_user
        data = lang_data.get(session_lang)
        user = {
            "phone_number": input(data.get("phone_number"))
        }
        session_user = User(**user).is_auth(session_lang)
        Account().main(session_user)
