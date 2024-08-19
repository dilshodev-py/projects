from models import User, ToDo
from datetime import datetime

session_user: None | User = None


class UserUI:
    def settings(self):
        global session_user
        menu = """
            1) My info
            2) Edit 
            3) Delete account
            0) <-back
            >>>"""
        key = input(menu)
        match key:
            case "1":
                print(session_user.__dict__)
                self.settings()
            case "2":
                self.edit()
            case "3":
                session_user.delete()
                session_user = None
                UI().main()
            case "0":
                UI().account()

    def edit(self):
        global session_user
        field = """
            1) fullname
            2) phone number
            3) password
            0) <-back
            """
        key = input(field)
        if key == "0":
            self.settings()
            return
        new_value = input("New Value : ")
        match key:
            case "1":
                User(id=session_user.id).update("fullname", new_value)
            case "2":
                User(id=session_user.id).update("phone_number", new_value)
            case "3":
                User(id=session_user.id).update("password", new_value)

        self.settings()


class ToDoUI:
    def create(self):
        todo = {
            "id": ToDo().sequence_id(),
            "title": input("Title : "),
            "body": input("Body : "),
            "date": input("Date : "),
            "status": False,
            "user_id": session_user.id
        }
        ToDo(**todo).save()
        UI().account()


    def my_todo(self):
        session_todos: list[ToDo] = ToDo(user_id= session_user.id).get_todo_list()
        for todo in session_todos:
            print(f"{todo.id}) {todo.title}")
        print("0) <-back")
        key = input(">>>")
        if key == "0":
            UI().account()
            return
        todo_id = int(key)
        self.crud(todo_id)

    def crud(self, todo_id):
        crud_menu = """
            1) show
            2) update
            3) delete
            0) <-back
            >>>"""
        key = input(crud_menu)
        match key:
            case "1":
                todo: ToDo = ToDo(id =todo_id ).get()
                print(todo.__dict__)
                self.crud(todo_id)
            case "2":
                self.update(todo_id)

            case "3":
                ToDo(id = todo_id).delete()
                self.my_todo()

            case "0":
                self.my_todo()

    def update(self , todo_id):
        fields = """
            1) title
            2) body
            3) date
            4) status
            0) <-back
            >>>"""
        key = input(fields)
        if key == "0":
            self.crud(todo_id)
            return
        new_value = input("new val : ")
        match key:
            case "1":
                ToDo(id = todo_id).update("title",new_value )
            case "2":
                ToDo(id=todo_id).update("body", new_value)
            case "3":
                ToDo(id=todo_id).update("date", new_value)
            case "4":
                ToDo(id=todo_id).update("status", new_value)
        self.crud(todo_id)

class UI:
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

    def login(self):
        global session_user
        auth_user = {
            "phone_number": input("Phone number : "),
            "password": input("Password : ")
        }
        auth = User(**auth_user)
        is_bool, response = auth.is_login()
        if is_bool:
            session_user = response
            self.account()
            return
        print(response)
        self.main()

    def register(self):
        user = {
            "id": User().sequence_id(),
            "fullname": input("Fullname : "),
            "phone_number": input("Phone : (+998) "),
            "password": input("password : "),
            "join_at": str(datetime.now())
        }
        user = User(**user)
        is_bool, message = user.is_valid()
        if is_bool:
            user.save()
        print(message)
        self.main()

    def account(self):
        global session_user
        menu = """
            1) ToDo
            2) My ToDo
            3) settings
            0) logout
            >>>"""
        key = input(menu)
        match key:
            case "1":
                ToDoUI().create()
            case "2":
                ToDoUI().my_todo()
            case "3":
                UserUI().settings()
            case "0":
                session_user = None
                self.main()

UI().main()
