"""TODO project"""
# auth
from typing import Optional

"""
    login
    register
"""
users: list['User'] = []
todos: list['ToDo'] = []

current_user: Optional['User'] = None


class BaseClass:
    def sequence_id(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_value):
        pass

    def get_all(self):
        pass


class User(BaseClass):
    def __init__(self,
                 id=None,
                 fullname=None,
                 username=None,
                 password=None
                 ):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def is_valid(self):
        for user in users:
            if user.username == self.username:
                return False, 'Already exists username'
        if len(self.password) < 4:
            return False, "Invalid password !"
        return True, "Success"

    def is_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return True, user
        return False, "Not Found"

    def sequence_id(self):
        return users[-1].id + 1 if users else 1

    def save(self):
        users.append(self)

    def delete(self):
        users.remove(self)

    def update(self, field, new_value):
        for user in users:
            if user.id == self.id:
                if field == 'fullname':
                    user.fullname = new_value
                elif field == 'password':
                    user.password = new_value
                elif field == 'username':
                    user.username = new_value


    def get_all(self):
        super().get_all()


class ToDo(BaseClass):
    def __init__(self,
                 id=None,
                 title=None,
                 description=None,
                 execute_at=None,
                 user_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.execute_at = execute_at
        self.user_id = user_id

    def sequence_id(self):
        return todos[-1].id + 1 if todos else 1

    def save(self):
        todos.append(self)

    def delete(self):
        for todo in todos:
            if todo.id == self.id:
                todos.remove(todo)
                return
        print("O'chiriladigan todo topilmadi")

    def update(self, field, new_value):
        for todo in todos:
            if todo.id == self.id:
                if field == "title":
                    todo.title = new_value
                elif field == 'description':
                    todo.description = new_value
                elif field == "execute_at":
                    todo.execute_at = new_value
                return
        print("Todo topilmadi")

    def get_all(self):
        result = []
        for todo in todos:
            if todo.user_id == self.user_id:
                result.append(todo)
        return result


class UI:
    def main(self):
        menu = """
        1) Register
        2) Login
        3) Exit
        >>>"""
        match input(menu):
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

    def account(self):
        print("Welcome account " + current_user.fullname)
        menu = """
        1) T0D0
        2) settings
        3) logout
        >>>"""
        match input(menu):
            case "1":
                self.todo_menu()
            case "2":
                self.settings()
            case "3":
                self.main()

    def register(self):
        user_dict = {
            "id": User().sequence_id(),
            "fullname": input("Fullname: "),
            "username": input("Username: "),
            "password": input("Password: ")
        }
        user = User(**user_dict)
        is_bool, message = user.is_valid()
        if is_bool == True:
            user.save()
        print(message)
        self.main()

    def login(self):
        global current_user
        auth = {
            "username": input("Username : "),
            "password": input("Password : ")
        }
        user = User(**auth)
        is_bool, response = user.is_login()
        if is_bool == True:
            current_user = response
            self.account()
            return
        print(response)
        self.main()

    def todo_menu(self):
        menu = """
        *) search
        1) create
        2) delete
        3) update
        4) get all
        0) <- back
        >>>"""
        match input(menu):
            case "*":
                pass
            case "1":
                todo = {
                    "id": ToDo().sequence_id(),
                    "title": input("Title : "),
                    "description": input("Description : "),
                    "execute_at": input("execute_at : "),
                    "user_id": current_user.id
                }
                todo = ToDo(**todo)
                todo.save()
            case "2":
                id = int(input("ID : "))
                ToDo(id=id).delete()
            case "3":
                id = int(input("ID :"))
                field = input("fields [title , description , execute_at] : ")
                new_value = input("New Value : ")
                ToDo(id=id).update(field, new_value)
            case "4":
                todo_list: list['ToDo'] = ToDo(user_id=current_user.id).get_all()
                for todo in todo_list:
                    print(f"{todo.id}) {todo.title}")

            case "0":
                self.account()
                return

        self.todo_menu()

    def settings(self):
        menu = """
            1) update profile
            2) delete account
            0) <- back
            >>>"""
        match input(menu):
            case "1":
                field = input("Field [fullname , username , password] : ")
                new_value = input("New Value : ")
                User(id = current_user.id).update(field , new_value)
                self.settings()
            case "2":
                current_user.delete()
                self.main()
            case "0":
                self.account()

UI().main()
