from projects.ToDo.exceptions import AuthException

users = []
tasks = []


class BaseModel:

    def __init__(self, id: int = None):
        self.id = id

    def delete(self):
        pass

    def update(self, field, new_value):
        pass

    def save(self):
        pass

    def get(self):
        pass


class User(BaseModel):
    def __init__(self,
                 id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 password: str = None
                 ):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def delete(self):
        for user in users:
            if user.id == self.id:
                users.remove(user)
                break

    def update(self, field, new_value):
        for user in users:
            if user.id == self.id:
                if field == "first_name":
                    user.first_name = new_value
                elif field == "last_name":
                    user.last_name = new_value
                elif field == "email":
                    user.email = new_value
                elif field == "password":
                    user.password = new_value

    def save(self):
        self.id = users[-1].id + 1 if users else 1
        users.append(self)

    def get(self):
        for user in users:
            if user.id == self.id:
                return user

    def is_valid(self):
        #  email unique
        #  password len
        for user in users:
            if user.email == self.email:
                raise AuthException("Already exists")
        if len(self.password) < 4:
            raise AuthException('Password must be at least 4 characters')


    def is_auth(self):
        for user in users:
            if user.email == self.email and user.password == self.password:
                return user
        raise AuthException("Not Found account")
