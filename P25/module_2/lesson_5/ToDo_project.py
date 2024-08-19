users: list['User'] = []
todos: list['ToDo'] = []


class CRUD:
    def sequence_id(self):
        pass

    def save(self):
        pass

    def update(self, attribute, new_value):
        pass

    def delete(self):
        pass

    def get_all(self):
        pass


class User(CRUD):
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 username: str = None,
                 password: str = None):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password


    def is_login(self):
        pass

    def is_valid(self):
        pass

    def sequence_id(self):
        super().sequence_id()

    def save(self):
        super().save()

    def update(self, attribute, new_value):
        super().update(attribute, new_value)

    def delete(self):
        super().delete()

    def get_all(self):
        super().get_all()


class ToDo(CRUD):

    def __init__(self,
                 id: int = None,
                 title: str = None,
                 description: str = None,
                 time: str = None,
                 user_id : int = None
                 ):
        self.id = id
        self.title = title
        self.description = description
        self.time = time
        self.user_id = user_id

    def sequence_id(self):
        super().sequence_id()

    def save(self):
        todos.append(self)

    def update(self, attribute, new_value):
        super().update(attribute, new_value)

    def delete(self):
        super().delete()

    def get_all(self):
        result = []
        for todo in todos:
            if todo.user_id == self.user_id:
                result.append(todo)
        return result



class UI:

    def register(self):
        user = {
            "id": User().sequence_id(),
            "fullname": input("Fullname : "),
            "username": input("Username : "),
            "password": input("Password : "),
        }
        user = User(**user)
        is_valid, message = user.is_valid()
        if is_valid:
            user.save()
        print(message)
        self.main()

    def login(self):
        auth = {
            "username": input("Username : "),
            "password": input("Password : "),
        }

        auth = User(**auth)
        is_bool , response = auth.is_login()
        if is_bool:
            current_user = response
            self.account(current_user)
            return
        print(response)
        self.main()

    def main(self):
        menu = """
            1) Register
            2) Login
            3) exit
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

    def account(self , current_user):
        menu = """
            1) Todo
            2) settings
            3) logout
            >>>"""
        key = input(menu)

        match key:
            case "1":
                self.todo_menu(current_user)
            case "2":
                pass
            case "3":
                self.main()


    def todo_menu(self ,current_user : User ):
        menu = """
            *) search
            1) create
            2) delete
            3) update
            4) get all
            5) <- back
            >>>"""
        key = input(menu)
        match key :
            case "*":
                pass
            case "1":
                todo = {
                    "id" : ToDo().sequence_id(),
                    "title" : input("Title : "),
                    "description" : input("Description : "),
                    "time" : input("Time : "),
                    "user_id" : current_user.id
                }
                todo = ToDo(**todo)
                todo.save()
            case "2":
                pass
            case "3" :
                pass
            case "4" :
                for todo in ToDo(user_id=current_user.id).get_all():
                    print(f"{todo.id}) {todo.title}")

            case "5":
                self.account(current_user)