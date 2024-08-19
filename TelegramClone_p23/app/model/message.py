from app.model.db_control import MessageDTO
from app.utils.main import CrudAbstract


class Message(MessageDTO, CrudAbstract):
    def save(self):
        messages: list[Message] = self.read()
        messages.append(self)
        self.write(messages)

    def update(self, field, new_val):
        messages: list[Message] = self.read()
        for message in messages:
            if message.id == self.id:
                if field == "chat_id":
                    message.chat_id = new_val
                if field == "message":
                    message.message = new_val
                if field == "type":
                    message.type = new_val
                if field == "datetime":
                    message.datetime = new_val

    def delete(self):
        messages: list[Message] = self.read()
        for message in messages:
            if message.id == self.id:
                messages.remove(message)

    def get(self):
        messages: list[Message] = self.read()
        for message in messages:
            if message.id == self.id:
                return message