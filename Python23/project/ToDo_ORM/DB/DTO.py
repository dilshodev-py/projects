from pydantic.v1 import BaseModel, validator

from project.ToDo_ORM.models.auth import User


class UserDTO(BaseModel):
    id: int = None
    first_name: str = None
    last_name: str = None
    email: str = None
    created_at: str = None

    @validator('email')
    @classmethod
    def validate_email(cls, value):
        if not value.endswith("@gmail.com"):
            raise Exception("emailda xatolik")
        users: list = User().select()
        for user in users:
            if user[3] == value:
                raise Exception("Bunday email mavjud")
        return value

    def save(self):
        User(first_name=self.first_name , last_name=self.last_name , email = self.email).insert()

    def all(self) -> list['UserDTO']:
        users: list = User().select()
        for i , data in users:
            users[i] = UserDTO(*data)
        return users

