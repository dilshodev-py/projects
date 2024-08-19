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
        users.remove(self)


    def save(self):
        users.append(self)

    def is_valid(self):
        if len(self.password) < 4:
            return False, 'Password must be at least 4 characters'
        return self.is_phone_number()




    def is_phone_number(self):
        for user in users:
            if user.phone_number == self.phone_number:
                return False, "Phone number is already taken."
        return True, "Success"



    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def is_login(self):
        for user in users:
            if user.phone_number == self.phone_number and user.password == self.password:
                return True, user
        return False, "Account not found"

    def update(self, field, new_val):
        for user in users:
            if user.id == self.id:
                if field == "fullname":
                    user.fullname = new_val
                if field == "phone_number":
                    user.phone_number = new_val
                if field == "password":
                    user.password = new_val



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
        todos.append(self)

    def sequence_id(self):
        return todos[-1].id + 1 if todos else 1

    def update(self, field, new_val):
        for todo in todos:
            if todo.id == self.id:
                if field == "title":
                    todo.title = new_val
                if field == "body":
                    todo.body = self.body
                if field == "datetime":
                    todo.datetime = new_val
                if field == "status":
                    todo.status = new_val

    def delete(self):
        todos.remove(self)
