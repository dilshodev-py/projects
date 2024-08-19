from db.config import DB
from models.DTO import *


class User(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        users = self.all()
        for i, user in enumerate(users):
            users[i] = UserDTO(*user)
        return users

    def object_filter(self, **cond):
        users = self.filter(**cond)
        for i ,user in enumerate(users):
            users[i] = UserDTO(*user)
        return users

    def is_unique_valid(self):
        phone = self.kwargs.get("phone_number")
        username = self.kwargs.get("username")
        users = self.object_all()
        for user in  users:
            if user.phone_number == phone or user.username == username:
                raise Exception("Already exits phone number or username !")



    def is_login(self):
        user = UserDTO(**self.kwargs)
        user = self.filter(phone_number=user.phone_number)
        if not user:
            raise Exception("Not Found")

        return UserDTO(*user[0])




class Channel(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        channels = self.all()
        for i, channel in enumerate(channels):
            channels[i] = ChannelDTO(*channel)
        return channels


class Channels_User(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        channel_users = self.all()
        for i, channel_user in enumerate(channel_users):
            channel_users[i] = ChannelsUsersDTO(*channel_user)
        return channel_users


class Contact(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        contacts = self.all()
        for i, contact in enumerate(contacts):
            contacts[i] = ContactsDTO(*contact)
        return contacts


class Group_User(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        group_users = self.all()
        for i, group_user in enumerate(group_users):
            group_users[i] = GroupUsersDTO(*group_users)
        return group_users


class Group(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        groups = self.all()
        for i, group in enumerate(groups):
            groups[i] = GroupsDTO(*group)
        return groups


class Message_Channel(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        message_channels = self.all()
        for i, message_channel in enumerate(message_channels):
            message_channels[i] = MessageChannelDTO(*message_channel)
        return message_channels


class Message_Channels_Statu(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        message_channels_status = self.all()
        for i, message_channels_st in enumerate(message_channels_status):
            message_channels_status[i] = MessageChannelStatusDTO(*message_channels_st)
        return message_channels_status


class Message_Group(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        message_groups = self.all()
        for i, message_group in enumerate(message_groups):
            message_groups[i] = MessageGroupDTO(*message_group)
        return message_groups


class Message_Groups_Statu(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        message_group_status = self.all()
        for i, message_group_st in enumerate(message_group_status):
            message_group_status[i] = MessageGroupStatusDTO(*message_group_st)
        return message_group_status


class Message_Personal(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def object_all(self):
        message_personals = self.all()
        for i, message_personal in enumerate(message_personals):
            message_personals[i] = MessageChannelDTO(*message_personal)
        return message_personals
