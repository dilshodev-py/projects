# CRUD
"""
Create
Read
Update
Delete
"""

"""
ToDo
    id
    title
    description
    execute_at  
"""

todos: list['ToDo'] = []

# backend
# frontend

class ToDo:
    def __init__(self,
                 id: int = None,
                 title: str = None,
                 description: str = None,
                 execute_at: str = None,
                 ):
        self.id = id
        self.title = title
        self.description = description
        self.execute_at = execute_at

    def sequence_id(self):
        return todos[-1].id + 1 if todos else 1

    def create(self):
        todos.append(self)

    def update(self, id_, attribute, new_value):
        for todo in todos:
            if todo.id == id_:
                if attribute == 'title':
                    todo.title = new_value
                elif attribute == 'description':
                    todo.description = new_value

                elif attribute == 'execute_at':
                    todo.execute_at = new_value



    def delete(self, id_):
        for todo in todos:
            if todo.id == id_:
                todos.remove(todo)

    def read(self):
        return todos

    def search(self, short_title):
        result = []
        for todo in todos:
            if todo.title.lower().startswith(short_title.lower()):
                result.append(todo)
        return result


while True:
    menu = """
        *) search
        1) create
        2) update
        3) delete
        4) read
        0) exit
        >>>"""
    key = input(menu)
    match key:
        case "*":
            short_title = input(">>>")
            ToDo().search(short_title)
        case "1":
            todo = {
                "id" : ToDo().sequence_id(),
                "title" : input("Title : "),
                "description" : input("Description : "),
                "execute_at" : input("Execute_at : ")
            }
            ToDo(**todo).create()
        case "2":
            id_ = int(input("ID"))
            attribute = input("Attribute : ")
            new_value = input("New value : ")
            ToDo().update(id_ , attribute , new_value)
        case "3":
            id_ = int(input("ID:"))
            ToDo().delete(id_)
        case "4":
            todo_list = ToDo().read()
            for todo in todo_list:
                print(f"{todo.id}) {todo.title} ")
        case "0":
            break
