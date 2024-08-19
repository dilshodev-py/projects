users: list['User'] = []
todos: list['ToDo'] = []


class User:
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 phone_number: str = None,
                 password: str = None,
                 join_at: str = None):
        self.id = id
        self.fullname = fullname
        self.phone_number = phone_number
        self.password = password
        self.join_at = join_at

    def delete(self):
        pass

    def save(self):
        pass

    def is_valid(self):
        pass

    def is_phone_number(self):
        pass

    def sequence_id(self):
        pass

    def is_login(self):
        pass

    def update(self, field, new_val):
        pass


class ToDo:

    def __init__(self,
                 id: int = None,
                 title: str = None,
                 body: str = None,
                 datetime: str = None,
                 status: str = None,
                 user_id: str = None,
                 ):
        self.id = id
        self.title = title
        self.body = body
        self.datetime = datetime
        self.status = status
        self.user_id = user_id

    def save(self):
        pass

    def sequence_id(self):
        pass

    def update(self, field, new_val):
        pass

    def delete(self):
        pass





