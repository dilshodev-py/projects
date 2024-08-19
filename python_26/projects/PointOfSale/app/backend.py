import datetime
from abc import ABC, abstractmethod

from projects.PointOfSale.db.db import DB


class ModelBase(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self, field, new_value):
        pass


class User(ModelBase, DB):
    def __init__(self,
                 id: int = '',
                 first_name: str = '',
                 last_name: str = '',
                 role: str = '',
                 phone_number: str = '',
                 password: str = '',
                 ball: int = 0,
                 group_id: str = '',
                 created_at: str = '',
                 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone_number = phone_number
        self.password = password
        self.ball = ball
        self.group_id = group_id
        self.created_at = created_at
    @classmethod
    def from_str(cls , data: str):
        return cls(*data.rstrip('\n').split('|'))

    def students_all(self):
        users: list[User] = self.objects
        students = []
        for user in users:
            if user.role == 'student':
                students.append(user)
        return students

    def get(self):
        users: list[User] = self.objects
        for user in users:
            if user.phone_number == self.phone_number:
                return user

    def is_auth(self):
        users: list[User] = self.objects
        for user in users:
            if user.phone_number == self.phone_number and user.password == self.password:
                return True, user
        return False, "Invalid password !"

    def exists(self):
        users: list[User] = self.objects
        for user in users:
            if user.phone_number == self.phone_number and user.password == '':
                return True
            elif user.phone_number == self.phone_number and user.password != '':
                return False

        return "Not Found account !"

    def save(self):
        users: list[User] = self.objects
        self.id = int(users[-1].id) + 1 if users else 1
        users.append(self)
        self.write(users)

    def delete(self):
        users: list[User] = self.objects
        for user in users:
            if user.id == self.id:
                users.remove(user)
        self.write(users)

    def update(self, field, new_value):
        users: list[User] = self.objects
        for user in users:
            if user.id == self.id:
                if field == 'first_name':
                    user.first_name = new_value
                elif field == 'last_name':
                    user.last_name = new_value
                elif field == 'age':
                    user.age = new_value
        self.write(users)


class Group(ModelBase, DB):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 status: str = None,
                 max_space: int = None,
                 is_full: bool = None,
                 ):
        self.id = id
        self.name = name
        self.status = status
        self.max_space = max_space
        self.is_full = is_full

    @classmethod
    def from_str(cls, data: str):
            return cls(*data.rstrip('\n').split('|'))

    def save(self):
        groups: list[Group] = self.objects
        self.id = int(groups[-1].id) + 1 if groups else 1
        groups.append(self)
        self.write(groups)

    def delete(self):
        groups: list[Group] = self.objects
        for group in groups:
            if group.id == self.id:
                groups.remove(group)
        self.write(groups)

    def update(self, field, new_value):
        groups: list[Group] = self.objects
        for group in groups:
            if group.id == self.id:
                if field == 'name':
                    group.name = new_value
                elif field == 'status':
                    group.status = new_value
                elif field == 'max_space':
                    group.max_space = new_value
        self.write(groups)

    def filter_group_all(self, incomplete=False, full=False , graduated = False):
        groups: list[Group] = self.objects
        result_groups = []
        for group in groups:
            if graduated and group.status == 'False':
                result_groups.append(group)
            elif incomplete and not group.is_full:
                result_groups.append(group)
            elif full and group.is_full:
                result_groups.append(group)

        return result_groups




class Subject(DB, ModelBase):
    def __init__(self,
                 id: None,
                 name: None):
        self.id = id
        self.name = name

    @classmethod
    def from_str(cls, data: str):
        return cls(*data.rstrip('\n').split('|'))

    def save(self):
        subjects: list[Subject] = self.objects
        self.id = int(subjects[-1].id) + 1 if subjects else 1
        subjects.append(self)
        self.write(subjects)

    def delete(self):
        subjects: list[Subject] = self.objects
        for subject in subjects:
            if subject.id == self.id:
                subjects.remove(subject)
        self.write(subjects)

    def update(self, field, new_value):
        subjects: list[Subject] = self.objects
        for subject in subjects:
            if subject.id == self.id:
                if field == 'name':
                    subject.name = new_value
        self.write(subjects)

# new_user = {
#     "first_name" : input("First name: "),
#     "last_name" : input("Last name: "),
#     "role" : input("Role: "),
#     "phone_number" : input("Phone_number: "),
#     "password" : input("Password: "),
#     "ball" : input("Ball: "),
#     "group_id" : input("Group_id: "),
#     "created_at" : str(datetime.datetime.now())[:-7],
# }
# User(**new_user).save()
