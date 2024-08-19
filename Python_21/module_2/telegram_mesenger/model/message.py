from datetime import datetime

from module_2.telegram_mesenger.model.tmp import MessageDTO, AbstractCRUD
from module_2.telegram_mesenger.model.user import User


class Message(MessageDTO, AbstractCRUD):
    def save(self):
        messages = self.messages_list()
        messages.append(self)
        MessageDTO.write(messages)

    def unread_message(self):
        count = 0
        messages = self.messages_list()
        for message in messages:
            if int(message.to_receiver_id) == int(self.send_user_id) and message.status == 'False':
                count += 1
        return count


    def update(self, filed, new_val):
        pass

    def delete(self):
        pass

    def get(self):
        pass

    def get_receiver(self):
        messages = self.messages_list()
        receivers = set()
        for message in messages:
            if message.type == self.type and (message.send_user_id == self.send_user_id):
                user_obj = User(message.to_receiver_id).get()
                receivers.add((user_obj.id , user_obj.username))
            elif message.type == self.type and (message.to_receiver_id == self.send_user_id):
                user_obj = User(message.send_user_id).get()
                receivers.add((user_obj.id, user_obj.username))

        return receivers

    def messages_list(self):
        return MessageDTO.read()

    def get_chat(self, receiver = False):
        result = []
        messages = self.messages_list()
        for message in messages:
            if message.to_receiver_id == self.to_receiver_id and message.send_user_id == self.send_user_id:
                if receiver:
                    message.status = True
                result.append(message)
        if receiver:
            MessageDTO().write(messages)
        return result

    def sequence_id(self):
        messages: list[MessageDTO] = self.messages_list()
        return int(messages[-1].id) + 1 if messages else 1



