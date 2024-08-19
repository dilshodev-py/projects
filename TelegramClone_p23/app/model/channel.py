from app.model.db_control import ChannelDTO
from app.utils.main import CrudAbstract


class Channel(ChannelDTO, CrudAbstract):
    def save(self):
        channels: list[Channel] = self.read()
        channels.append(self)
        self.write(channels)

    def delete(self):
        channels: list[Channel] = self.read()
        for channel in channels:
            if channel.id == self.id:
                channels.remove(channel)

    def get(self):
        channels: list[Channel] = self.read()
        for channel in channels:
            if channel.id == self.id:
                return channel

    def update(self, field, new_val):
        channels: list[Channel] = self.read()
        for channel in channels:
            if channel.id == self.id:
                if field == "username":
                    channel.username = new_val
                if field == "name":
                    channel.name = new_val
                if field == "status":
                    channel.status = new_val
                if field == "link":
                    channel.link = new_val
                if field == "bio":
                    channel.bio = new_val
                if field == "photo":
                    channel.photo = new_val

