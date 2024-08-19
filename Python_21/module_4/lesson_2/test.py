"""psycopg2-binary"""
"""
pip install psycopg2-binary
"""
#
# import psycopg2
#
# connect = psycopg2.connect(
#     database="lesson_2",
#     user="postgres",
#     password="1",
#     host="localhost",
#     port=5432)
#
# cursor = connect.cursor()
#
# query = """
# delete from users where id = %s;
# """
# cursor.execute(query, (5,))
# connect.commit()
# users = cursor.fetchall()
# print(users)
#
# for user in users:
#     print(user[1])

"""
[
    (1, 'Botir', 24, datetime.date(2000, 12, 1) ),
    (3, "Jo'rabek", 13, datetime.date(2011, 12, 1) ),
    (5, 'Polat', 13, datetime.date(2011, 12, 1) ), 
    (4, 'Botir', 13, datetime.date(2011, 12, 1) )]
"""


