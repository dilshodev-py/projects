DB_PATH = "/home/dilshod/PycharmProjects/TelegramClone_p23/app/database/"


class File:

    @classmethod
    def read(cls):  # Channel
        file_name = cls.__name__.lower() + "s.txt"
        with open(f"{DB_PATH}/{file_name}", 'r') as f:
            data = f.read().split('\n')
        if '' in data:
            del data[0]
        result = []
        for i in data:
            obj = cls(*i.split('|'))
            result.append(obj)
        return result

    @classmethod
    def write(cls, objects: list):
        file_name = cls.__name__.lower() + "s.txt"

        for i, obj in enumerate(objects):
            objects[i] = "|".join(map(str, obj.__dict__.values()))
        data = "\n".join(objects)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write(data)


class UserDTO(File):
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 phone_number: str = None,
                 username: str = None,
                 photo: str = None,
                 bio: str = None,
                 ):
        self.id = id
        self.fullname = fullname
        self.phone_number = phone_number
        self.username = username
        self.photo = photo
        self.bio = bio


class ContactDTO(File):
    def __init__(self,
                 id: int = None,
                 user_id: int = None,
                 owner_id: int = None):
        self.id = id
        self.user_id = user_id
        self.owner_id = owner_id


class ChannelDTO(File):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 username: str = None,
                 status: str = None,
                 link: str = None,
                 bio: str = None,
                 photo: str = None,
                 admin_id: int = None):
        self.id = id
        self.name = name
        self.username = username
        self.status = status
        self.link = link
        self.bio = bio
        self.photo = photo
        self.admin_id = admin_id


class GroupDTO(File):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 username: str = None,
                 status: str = None,
                 bio: str = None,
                 link: str = None,
                 photo: str = None,
                 admin_id: int = None):
        self.id = id
        self.name = name
        self.username = username
        self.status = status
        self.bio = bio
        self.link = link
        self.photo = photo
        self.admin_id = admin_id


class GroupMemberDTO(File):
    def __init__(self,
                 id: int = None,
                 user_id: int = None,
                 group_id: int = None):
        self.id = id
        self.user_id = user_id
        self.group_id = group_id


class ChannelMemberDTO(File):
    def __init__(self,
                 id: int = None,
                 user_id: int = None,
                 channel_id: int = None):
        self.id = id
        self.user_id = user_id
        self.channel_id = channel_id


class MessageDTO(File):
    def __init__(self,
                 id: int = None,
                 chat_id: int = None,
                 message: str = None,
                 type: str = None,
                 datetime: str = None):
        self.id = id
        self.chat_id = chat_id
        self.message = message
        self.type = type
        self.datetime = datetime
