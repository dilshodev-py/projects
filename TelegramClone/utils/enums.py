from enum import Enum


class StatusEnum(Enum):
    PUBLIC = 1
    PRIVATE = 2


class RoleEnum(Enum):
    ADMIN = 'Admin'
    USER = 'User'
