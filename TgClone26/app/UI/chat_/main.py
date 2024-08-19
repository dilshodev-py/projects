import datetime
from typing import Optional


from app.backend.backend import User, Chat


class ChatUI:
    def main(self, session= None):
        from app.UI.account_ import Account
        self.session_user = session

        print("\t\t\t\tChat Menu\n\n")
        print("*) search messanger")

        for user in Chat(sender_id = self.session_user.id).self_chat_list():
            print(f"{user.id}: {user.first_name}")
        print("0) Back")
        key = input(">>>")
        if key == "*":
            pass
        elif key == "0":
            Account().main(session_user = self.session_user)
        else:
            key = int(key)
            chats = Chat(sender_id = self.session_user.id,receiver_id= key).chat_messages()
            self.show_chat(chats ,key )


    def show_chat(self , chats , reciver_id):
        chats = sorted(list(chats), key= lambda x : datetime.datetime.fromisoformat(x.send_at))
        for chat in chats:
            if self.session_user.id == chat.sender_id:
                print(f'\t\t\t\t{chat.message}')
            else:
                print(f'{chat.message}')

        message = input("send >>>")
        Chat(sender_id = self.session_user.id,receiver_id= reciver_id , message = message).save()
        self.main(session=self.session_user)









