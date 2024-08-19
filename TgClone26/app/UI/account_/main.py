from typing import Optional
from app.UI.channel_.main import ChannelUI
from app.UI.chat_.main import ChatUI
from app.UI.contact_.main import ContactUI
from app.UI.group_.main import GroupUI
from app.backend.backend import User
from app.backend.enum_class import Lang, images
from app.backend.errors import UserError
from app.language.lang import lang_data


class Account:
    def main(self ,session_user = None, back=False):
        self.session_user = session_user
        data = lang_data.get(self.session_user.lang)  # noqa
        if not back:
            print("{welcome} {first_name_}".format(first_name_=self.session_user.first_name, **data))  # noqa
        menu = """
            1) {chat} (+0)
            2) {group} (+0)
            3) {channel} (+0)
            4) {contact}
            5) {settings}
            0) {logout}
            >>>"""
        match input(menu.format(**data)):
            case "1":
                ChatUI().main(session=self.session_user)
            case "2":
                GroupUI().main()

            case "3":
                ChannelUI().main()
            case "4":
                ContactUI().main()
            case "5":
                self.settings()
            case "0":

                self.session_user = None
                UI().main()

    def choose_lang(self):
        for lang in Lang:
            print(f"{lang.value}) {lang.name}")
        select = int(input(">>>"))
        return Lang(select).name

    def choose_image(self):
        for pos, image in images.items():
            print(f"{pos}) {image}")
        select = int(input(">>>"))
        return images.get(select)

    def input_username(self):
        data = lang_data.get(self.session_user.lang)
        tmp = input('{username}'.format(**data))
        if tmp == '':
            return self.session_user.username
        else:
            User(username=tmp).is_unique(self.session_user.lang, username=True)
        return tmp

    def settings(self):
        from app.UI.main import UI
        data = lang_data.get(self.session_user.lang)
        menu = """
            1) {edit}
            2) {language}
            3) {delete_account}
            0) {back}
            >>>"""
        match input(menu.format(**data)):
            case "1":
                try:
                    user = {
                        "first_name": self.session_user.first_name if (tmp := input(
                            '{first_name}'.format(**data))) == '' else tmp,
                        "last_name": self.session_user.last_name if (tmp := input(
                            '{last_name}'.format(**data))) == '' else tmp,
                        "username": self.input_username(),
                        "image": self.session_user.image if input('Image edit? [Y/n]') == 'n' else self.choose_image(),
                        "phone_number": self.session_user.phone_number if (tmp := input(
                            '{phone_number}'.format(**data))) == '' else tmp,
                        "bio": self.session_user.bio if (tmp := input('{bio}'.format(**data))) == '' else tmp,
                        "birthdate": self.session_user.birthdate if (tmp := input(
                            '{birthdate}'.format(**data))) == '' else tmp

                    }
                except UserError as e:
                    print(e)
                    self.settings()
                    return
                else:
                    self.session_user = self.session_user.update(**user)
                    self.settings()
            case "3":
                if input("{is_accept}".format(**data)) in ("yes", 'ha'):
                    self.session_user.delete()
                    UI().main()
                    return
                self.settings()
            case "2":
                lang = self.choose_lang()
                self.session_user = self.session_user.update(lang=lang)
                self.settings()
            case "0":
                self.main(back=True)
