import datetime

import psycopg2


class DB:
    con = psycopg2.connect(
        dbname='lesson_6',
        user='postgres',
        password='1',
        host='localhost',
        port=5432
    )
    cur = con.cursor()

    def update(self):
        pass

    def delete(self):
        pass

    def all(self):
        table_name = f"{self.__class__.__name__.lower()}s"
        fields = " , ".join(self.args) if self.args else "*"  # "id , name"

        query = f"""
            select {fields} from {table_name};
        """
        self.cur.execute(query)
        data = self.cur.fetchall()
        return data

    def filter(self, **cond):
        fields = " , ".join(self.args) # id , name
        table_name = self.__class__.__name__.lower() + "s"
        params = tuple(cond.values())
        cond = " = %s and ".join(cond.keys()) + '= %s'

        query = f"""
            select {fields} from {table_name} where {cond}
        """
        self.cur.execute(query , params)
        return self.cur.fetchall()

    def save(self):
        table_name = self.__class__.__name__.lower() + "s"
        fields = " , ".join(self.kwargs.keys()) #
        values = " , ".join(["%s"]*len(self.kwargs))
        params = tuple(self.kwargs.values())
        query = f"""
            insert into {table_name} ({fields})
            values ({values})
        """
        self.cur.execute(query, params)
        self.con.commit()



class Course(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class Student(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class Group(DB):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


# c = Course("course_id","name").filter(course_id=1)
# Course(name = "Tarix" , created_at = datetime.date.today()).save()
# Student(first_name = "Botir" , last_name = "Qayumov" , email = "botir@gmail.com" , course_id = 1 , created_at = datetime.date.today()).save()