class UserDTO:
    def __init__(self,
                 id=None,
                 fullname=None,
                 phone_number=None,
                 username=None,
                 photo=None,
                 bio=None,
                 ):
        self.id = id
        self.fullname = fullname
        self.phone_number = phone_number
        self.username = username
        self.photo = photo
        self.bio = bio


class ChannelDTO:
    def __init__(self,
                 id_=None,
                 name=None,
                 username=None,
                 status=None,
                 link=None,
                 description=None,
                 photo=None,
                 owner_id=None):
        self.id = id_
        self.name = name
        self.username = username
        self.status = status
        self.link = link
        self.description = description
        self.photo = photo
        self.owner_id = owner_id


class ChannelsUsersDTO:
    def __init__(self,
                 id_=None,
                 channel_id=None,
                 user_id=None,
                 role=None
                 ):
        self.id = id_
        self.channel_id = channel_id
        self.user_id = user_id
        self.role = role


class ContactsDTO:
    def __init__(self,
                 id_=None,
                 owner_id=None,
                 fullname=None,
                 user_id=None
                 ):
        self.id = id_
        self.owner_id = owner_id
        self.fullname = fullname
        self.user_id = user_id


class GroupUsersDTO:
    def __init__(self,
                 id_=None,
                 group_id=None,
                 user_id=None,
                 role=None
                 ):
        self.id = id_
        self.group_id = group_id
        self.user_id = user_id
        self.role = role


class GroupsDTO:
    def __init__(self,
                 id_=None,
                 name=None,
                 subject_id=None,
                 teacher_id=None
                 ):
        self.id = id_
        self.name = name
        self.subject_id = subject_id
        self.teacher_id = teacher_id


class MessageChannelDTO:
    def __init__(self,
                 id_=None,
                 message=None,
                 receiver_id=None,
                 sender_id=None,
                 status=None):
        self.id = id_
        self.message = message
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.status = status


class MessageChannelStatusDTO:
    def __init__(self, id_=None, channel_id=None, message_id=None, user_id=None):
        self.id = id_
        self.channel_id = channel_id
        self.message_id = message_id
        self.user_id = user_id


class MessageGroupDTO:
    def __init__(self, id_=None, message=None, group_id=None, user_id=None):
        self.id = id_
        self.message = message
        self.group_id = group_id
        self.user_id = user_id


class MessageGroupStatusDTO:
    def __init__(self, id_=None, group_id=None, message_id=None, user_id=None):
        self.id = id_
        self.group_id = group_id
        self.message_id = message_id
        self.user_id = user_id


class MessagePersonalDTO:
    def __init__(self, id_=None, message=None, receiver_id=None, sender_id=None, status=None):
        self.id = id_
        self.message = message
