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
        "courses_id": []
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
    "courses_id" : 2
}
"""

"""
{
    "id" : 1,
    "name" : "nomi",  # unique
    "number_of_students" : "studentlar soni",
    "is_active" : True or False,
}
"""

courses: list[dict] = []
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
                 courses_id=[]
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
                return False , "Already exits username"
        return True , "Success add !"

    def is_auth(self):
        for user in users:
            if user.get("username") == self.username and user.get("password") == self.password:
                return user
        return "Not Found Account"

    def save(self):
        users.append(self.__dict__)


    def add_courses_id(self, course_id):
        for user in users:
            if user.get("id") == self.id:
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

    def self_courses(self, courses_list):
        result = []
        for course in courses:
            if course.get("id") in courses_list:
                result.append(course)
        return result


    def active_courses(self):
        result = []
        for course in courses:
            if course.get("is_active"):
                result.append(course)
        return result

    def sequence_id(self):
        return courses[-1].get("id") + 1 if courses else 1

    def save(self):
        courses.append(self.__dict__)

    def is_exists(self):
        for course in courses:
            if course.get("name") == self.name:
                return False , "Already Exists Course name !"
        return True , "Success Add!"

    def course_list(self):
        return courses

    def student_course(self, course_id):
        result = []
        for user in users:
            if course_id in user.get("courses_id"):
                result.append(user)
        return result


        # number_of_students


class Admin:
    def admin_account(self):
        global session_user
        menu = """
            1) Course add
            2) Show Students
            0) logs out
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.course_add()
            case "2":
                for course in courses:
                    print(f"{course.get('id')}) {course.get('name')}")
                course_id = int(input(">>>"))
                students: list[dict] = Course().student_course(course_id)
                for student in students:
                    print(f"{student.get('id')}) {student.get('first_name')} {student.get('last_name')}")
                self.admin_account()

            case "0":
                UI().main()

    def course_add(self):
        course = {
            "id" : Course().sequence_id(),
            "name" : input("Course Name : ")
        }
        course = Course(**course)
        is_exists , message = course.is_exists()
        if is_exists:
            course.save()
        print(message)
        self.admin_account()




class UI:

    def choose_course(self) -> int:
        pass

    def register(self):
        user = {
            "id" : User().sequence_id(),
            "first_name" : input("first_name : "),
            "last_name" : input("last_name : "),
            "birth_day" : input("birth_day : "),
            "phone" : input("phone : "),
            "username" : input("username : "),
            "password" : input("password : "),
            "courses_id" : [self.choose_course()],
        }
        user = User(**user)
        is_exists , message = user.check_username()
        if is_exists:
            user.save()
        print(message)
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
        user = {
            "username" : input("Username : "),
            "password" : input("Password : "),
        }
        user = User(**user)
        response : dict | str = user.is_auth()
        if isinstance(response, dict):
            session_user = response
            if session_user.get("roll") == "ADMIN":
                Admin().admin_account()
            else:
                Student().student_menu()
        else:
            print(response)






class Student:

    def active_course_show(self):
        for course in courses:
            if course.get("is_active"):
                print(f"{course.get('id')}) {course.get('name')}")

    def join_course(self):
        self.active_course_show()
        course_id = int(input(">>>"))
        User(id = session_user.get("id")).add_courses_id(course_id)
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
                for i in Course().active_courses():
                    print(f"{i.get('id')}) {i.get('name')}")
                self.student_menu()
            case "2":
                self.join_course()
            case "3":
                for i in Course().self_courses(session_user.get("courses_id")):
                    print(f"{i.get('id')}) {i.get('name')}")
                self.student_menu()
            case "0":
                UI().main()

UI().main()

# TIME : 16:30
