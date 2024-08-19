users: list[dict] = [
    {
        "id": 1,
        "first_name": "admin",
        "last_name": "admin",
        "birth_day": "2000-01-01",
        "phone": "+998993456789",
        "username": "admin",  # unique
        "password": "admin_01",
        "roll": "ADMIN",
        "course_id": []
    }
]
"""
{
    "id" : 1,
    "first_name" : "ism",
    "last_name" : "familya",
    "birth_day" : "2000-01-01",
    "phone" : "+998993456789",
    "username" : "username", # unique
    "password" : "admin_01", 
    "roll" : "ADMIN" or "STUDENT",
    "course_id" : 2
}
"""

courses: list[dict] = []

"""
{
    "id" : 1,
    "name" : "nomi",  # unique
    "number_of_students" : "studentlar soni",
    "is_active" : True or False,
}
"""

session_user: dict | None = None


class User:
    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 birth_day=None,
                 phone=None,
                 username=None,
                 password=None,
                 roll="STUDENT",
                 courses_id=None
                 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birth_day
        self.phone = phone
        self.username = username
        self.password = password
        self.roll = roll
        self.courses_id = courses_id

    def sequence_id(self):
        return users[-1].get("id") + 1 if users else 1

    def check_username(self):
        for user in users:
            if user.get("username") == self.username:
                return False, "Already exits username !"
        return True, "Success save"

    def is_auth(self):
        for user in users:
            if user.get("username") == self.username and user.get("password") == self.password:
                return user

    def save(self):
        users.append(self.__dict__)

    def is_admin(self):
        for user in users:
            if user.get("roll") == "ADMIN":
                return True
        return False

    def add_courses_id(self, course_id):
        for user in users:
            if user.get("id") == self.id:
                # user["courses_id"] = user.get("courses_id").append(course_id)
                user["courses_id"] += [course_id]
class Course:

    def __init__(self,
                 id=None,
                 name=None,
                 number_of_students=0,
                 is_active=True):
        self.id = id
        self.name = name
        self.number_of_students = number_of_students
        self.is_active = is_active

    def self_courses(self, student_id):
        courses_list = []
        for user in users:
            if user.get("id") == student_id:
                courses_list = user.get("courses_id")
        for c in courses:
            if c.get("id") in courses_list:
                print(f"{c.get('id')}) {c.get('name')}")


    def active_courses(self):
        result = []
        for c in courses:
            if c.get("is_active"):
                result.append(c)
        return result

    def sequence_id(self):
        return courses[-1].get("id") + 1 if courses else 1

    def save(self):
        courses.append(self.__dict__)

    def is_exists(self):
        for course in courses:
            if course.get("name") == self.name:
                return False, "Already exits course name !"
        return True, "Success save course"

    def course_list(self):
        return courses

    def student_course(self, course_id):
        result = []
        for user in users:
            if user.get("course_id") == course_id:
                result.append(user)

        return result

        # number_of_students
class Admin:
    def admin_account(self):
        global session_user
        menu = """
            1) Course add
            2) SHow Students
            0) logs out
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.course_add()
            case "2":
                pass
            case "0":
                UI().main()
                session_user = None

    def course_add(self):
        course = {
            "id": Course().sequence_id(),
            "name": input("Name : ")
        }
        course = Course(**course)
        is_exist, message = course.is_exists()
        if is_exist:
            course.save()
        print(message)
        self.admin_account()
class UI:

    def choose_course(self) -> int:
        for c in Course().course_list():
            print(f"{c.get('id')}) {c.get('name')}")
        course_id = int(input(">>>"))
        return course_id

    def register(self):
        user = {
            "id": User().sequence_id(),
            "first_name": input("First name : "),
            "last_name": input("Last name : "),
            "birth_day": input("Birth day [YY:MM:DD] : "),
            "phone": input("Phone number (+998): "),
            "username": input("Username : "),
            "password": input("Password : "),
            "courses_id": [self.choose_course()],
        }

        user = User(**user)
        response = user.check_username()
        if response[0]:
            user.save()
        print(response[1])
        self.main()

    def main(self):
        menu = """
            1) Sign up
            2) Sign in
            3) exit
            >>>"""
        key: str = input(menu)
        match key:
            case "1":
                self.register()

            case "2":
                self.login()
            case "3":
                return

    def login(self):
        global session_user
        auth = {
            "username": input("username : "),
            "password": input("password : ")
        }
        user = User(**auth)
        if user:
            session_user = user.is_auth()
            if session_user.get("roll") == "ADMIN":
                Admin().admin_account()
                return
            else:
                Student().student_menu()
                return
        print("Not Found account !")
        self.main()
class Student:

    def active_course_show(self):
        courses = Course().active_courses()
        for c in courses:
            print(f"{c.get('id')}) {c.get('name')}")

    def join_course(self):
        self.active_course_show()
        course_id = int(input(">>>"))
        User(id=session_user.get("id")).add_courses_id(course_id)
        self.student_menu()

    def student_menu(self):
        global session_user
        menu = """
            1) Course list (+active)
            2) Join to course
            3) Self courses
            0) logs out
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.active_course_show()
            case "2":
                self.join_course()
            case "3":
                Course().self_courses(session_user.get("id"))
                self.student_menu()
            case "0":
                UI().main()
                session_user = None

UI().main()
