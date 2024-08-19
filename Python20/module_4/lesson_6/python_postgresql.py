import psycopg2


# pip install psycopg2-binary
from datetime import date
con = psycopg2.connect(
    dbname = 'lesson_6',
    user = 'postgres',
    password = '1',
    host = 'localhost',
    port = 5432
)
cursor = con.cursor()



query  ="""
insert into courses (name ,created_at )
values (%s , %s);
"""

params = ('Math' , '2024-02-01')

cursor.execute(query,params )
con.commit()
# courses = cursor.fetchall()
# for course in courses:
#     print(course[1])
#
# Student.firstname , Student.email
