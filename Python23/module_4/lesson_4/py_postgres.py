# import psycopg2  # py + postgres - connection
#
# connection = psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     host="localhost",
#     port=5432,
#     password=1
# )
#
# console = connection.cursor()
# delete_query = "delete from categories where id = 2"
# select_query = "select * from categories"
# category = input("Category : ")
# insert_query = f"insert into categories(name) values (%s)"
# params = (category,)
# console.execute(insert_query, params)
# connection.commit()
# for i in console.fetchone():
#     print(i)




