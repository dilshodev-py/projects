
"""
ToDo
    id
    title
    description
    execute_at
"""
"""
Create
Read
Update
Delete
"""

# todo - qilinadigan ish
todos: list['ToDo'] = []


class ToDo:
    def __init__(self,
                 id: int = None,
                 title: str = None,
                 description: str = None,
                 execute_at: str = None):
        self.id = id
        self.title = title
        self.description = description
        self.execute_at = execute_at

    def sequence_id(self):
        return todos[-1].id + 1 if todos else 1

    def search(self , short_title):
        result = []
        for todo in todos:
            if todo.title.lower().startswith(short_title.lower()):
                result.append(todo)
        return result


    def read(self):
        return todos

    def delete(self):
        for todo in todos:
            if todo.id == self.id:
                todos.remove(todo)

    def update(self, attribute, new_value):
        for todo in todos:
            if todo.id == self.id:
                if attribute == "title":
                    todo.title = new_value
                elif attribute == 'description':
                    todo.description = new_value
                elif attribute == "execute_at":
                    todo.execute_at = new_value

    def create(self):
        todos.append(self)


while True:
    menu = """
        *) search
        1) create
        2) delete
        3) update
        4) read
        0) exit
        >>>"""
    key = input(menu)
    match key:
        case "*":
            short_title = input("Short title : ")
            todo_list = ToDo().search(short_title)
            for todo in todos:
                print(f"{todo.id}) {todo.title}")
        case "1":
            todo_dict = {
                "id": ToDo().sequence_id(),
                "title": input("Sarlovha : "),
                "description": input("Izoh : "),
                "execute_at": input("bajarish vaqti : "),
            }
            todo = ToDo(**todo_dict)
            todo.create()
        case "2":
            delete_id  = int(input("ID: "))
            ToDo(id = delete_id).delete()
        case "3":
            update_id = int(input("ID: "))
            attribute = input("[title , description , execute_at] >>>")
            new_value = input("New value : ")
            ToDo(id = update_id).update(attribute , new_value)
        case "4":
            todo_list = ToDo().read()
            for todo in todo_list:
                print(f"{todo.id}) {todo.title}")
        case "0":
            break

