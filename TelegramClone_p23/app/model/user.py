from app.errors.main import UserValidError
from app.model.db_control import UserDTO
from app.utils.main import CrudAbstract


class User(UserDTO, CrudAbstract):


    @property
    def sequence_id(self):
        users: list[User] = self.read()
        return int(users[-1].id) + 1 if users else 1

    def is_valid(self):
        if len(self.phone_number) != 13:
            raise UserValidError("Invalid phone number")
        self.is_unique_field()

    @property
    def is_login(self):
        users: list[User] = self.read()
        for user in users:
            if user.phone_number == self.phone_number:
                return user
        raise UserValidError("Not Found Account ! ")

    def search_users(self, search_username):
        users : list[User] = self.read()
        result = []
        for user in users:
            if user.username.lower().startswith(search_username.lower()):
                result.append(user)
        return result


    def is_unique_field(self):
        users: list[User] = self.read()
        for user in users:
            if user.phone_number == self.phone_number:
                raise UserValidError("Already exists phone number !")
            if user.username == self.username:
                raise UserValidError("Already exists Username !")

    def save(self):
        users: list[User] = self.read()
        users.append(self)
        self.write(users)

    def delete(self):
        users: list[User] = self.read()
        for user in users:
            if user.id == self.id:
                users.remove(user)
        self.write(users)

    def update(self, field, new_val):
        users: list[User] = self.read()
        for user in users:
            if user.id == self.id:
                if field == "fullname":
                    user.fullname = new_val
                if field == "phone_number":
                    user.phone_number = new_val
                if field == "username":
                    user.username = new_val
                if field == "photo":
                    user.photo = new_val
                if field == "bio":
                    user.bio = new_val
        self.write(users)

    def get(self):
        users: list[User] = self.read()
        for user in users:
            if user.id == self.id:
                return user


if __name__ == "__main__":
    u = User(1, "Kamol", "+998990000101", "kamol", "😂", "strong junior")
    users: list[User] = u.read()
    users.append(u)
    u.write(users)
