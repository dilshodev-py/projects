from module_3.lesson_4.ToDo.config import Hash
from module_3.lesson_4.ToDo.errors.main import ErrorMessage
from module_3.lesson_4.ToDo.model.db_control import File






class User(File):
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 email: str = None,
                 password: str = None,
                 join_at: str = None):
        self.id = id
        self.fullname = fullname # length(word) == 2
        self.email = email # unique
        self.password = password # length > 4
        self.join_at = join_at

    async def sequence_id(self):
        pass

    async def is_unique_email(self):
        pass

    def is_valid(self):
        pass

    def save(self):
        pass

    def is_auth(self):
        pass


    def __repr__(self):
        return f"{self.fullname}"

