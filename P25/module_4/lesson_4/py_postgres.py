# python+postgresql
# pip install psycopg2-binary
# import psycopg2
#
# connection = psycopg2.connect(
#     dbname='lesson_4',
#     user='postgres',
#     port=5432,
#     host='localhost',
#     password='1')
#
# console = connection.cursor()
#
# query = """
# select * from authors
# """
import psycopg2


# query = """
# insert into authors (name) values (%s)
# """

# console.execute(query)
# connection.commit()
# print(console.fetchone())
# print(console.fetchall())


# AUTHOR
# CRUD function
# class Authors:
#     connection = psycopg2.connect(
#         dbname='lesson_4',
#         user='postgres',
#         port=5432,
#         host='localhost',
#         password='1'
#     )
#     cursor = connection.cursor()
#
#     def __init__(self, name):
#         self.name = name
#
#     def create(self):
#         query = """
#         insert into authors (name) values (%s)
#         """
#         self.cursor.execute(query, (self.name,))
#         connection.commit()
#
#     def read(self):
#         query = """
#         select * from authors
#         """
#         self.cursor.execute(query)
#         return self.cursor.fetchall()
#
#     def update(self, author_id, name):
#         self.query = """
#         update authors
#         set name = %s where id = %s
#         """
#         self.cursor.execute(query, (name, author_id))
#         self.connection.commit()
#
#     def delete(self, author_id):
#         query = """
#         delete from authors where id = %s
#         """
#         self.cursor.execute(query, (author_id,))
#         self.connection.commit()

class DB:
    connection = psycopg2.connect(
        database="lesson_4",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

    def delete(self):
        table_name = self.__class__.__name__.lower() + "s"
        query = f"""
        delete from {table_name} where id = %s
        """
        self.cursor.execute(query, (self.id,))
        self.connection.commit()

    def insert(self):
        table_name = self.__class__.__name__.lower() + "s"
        cols = [k for k, v in self.__dict__.items() if v is not None]
        formats = " , ".join(['%s'] * len(cols))
        col_names = " , ".join(cols)
        params = tuple([v for v in self.__dict__.values() if v is not None])
        query = f"""
                insert into {table_name} ({col_names}) values ({formats})
                """
        self.cursor.execute(query, params)
        self.connection.commit()

    def select(self):
        pass

    def update(self, **kwargs):
        pass


class Author(DB):
    def __init__(self,
                 id: int = None,
                 name: str = None):
        self.id = id
        self.name = name


# class Book(DB):
#     def __init__(self,
#                  id: int = None,
#                  name: str = None,
#                  author: str = None):
#         self.id = id
#         self.name = name
#         self.author = author


# Author(id = 105).delete()
# Author(id = 1,name = 'CHingiz').insert()
# Author(id = 2).update(name = 'CHingiz')
# Author().select(id = 2)

# Book(name = "Oq kema" , author="CHingiz Aytmatov").insert()
# Book(id=1).delete()
