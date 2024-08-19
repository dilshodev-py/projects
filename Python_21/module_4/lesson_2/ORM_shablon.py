# import psycopg2

# class DB:
#     con = psycopg2.connect(
#         database="lesson_2",
#         user="postgres",
#         password="1",
#         host="localhost",
#         port=5432)
#
#     cur = con.cursor()
#
#     def insert(self):
#         table_name = self.__class__.__name__.lower() + "s"
#         columns_name = " , ".join(self.__dict__.keys())
#         params = tuple(self.__dict__.values())
#         formats = " , ".join(['%s'] * len(columns_name.split(',')))
#         query = f"""
#             insert into {table_name} ({columns_name})
#             values ({formats})
#         """
#         self.cur.execute(query, params)
#         self.con.commit()
#
#     def update(self, **conditions):
#         class_self = dict(self.__dict__)
#         del class_self['param']
#         table_name = self.__class__.__name__.lower() + "s"
#         set_field = " = %s , ".join([k for k, v in class_self.items() if not v is None]) + " = %s"
#         cond = " = %s and ".join(conditions.keys()) + " = %s"
#         params = [i for i in class_self.values() if not i is None] + list(conditions.values())
#         query = f"""
#             update {table_name} set {set_field} where {cond}
#         """
#         self.cur.execute(query, params)
#         self.con.commit()
#
#     def delete(self, **conditions):
#         cond = " = %s and ".join(conditions.keys()) + " = %s"
#         params = tuple(conditions.values())
#         table_name = self.__class__.__name__.lower() + "s"
#
#         query = f"""
#             delete from {table_name} where {cond};
#         """
#         self.cur.execute(query, params)
#         self.con.commit()
#
#     def select(self, **conditions):
#         table_name = self.__class__.__name__.lower() + "s"
#         columns = "*" if not self.param else " , ".join(self.param)
#         condition = "where " + " = %s and ".join(conditions.keys()) + " = %s" if conditions else ''
#         params = tuple(conditions.values())
#         query = f"""
#             select {columns} from {table_name} {condition}
#         """
#         self.cur.execute(query, params)
#         data = self.cur.fetchall()
#         return data
#
#
# class UserDTO:
#     def __init__(self, id= None, name= None, age = None, birthday = None):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.birthday = birthday


# class User(DB):
#     def __init__(self,
#                  *param,
#                  name=None,
#                  age=None,
#                  birthday=None):
#         self.param = param
#         self.name = name
#         self.age = age
#         self.birthday = birthday
#
#     def users_object(self , **cond):
#         users = User(*self.param).select(**cond)
#         for i , user in enumerate(users):
#             users[i] = UserDTO(*user)
#         return users


# class Product(DB):
#     def __init__(self, name=None, term=None):
#         self.name = name
#         self.term = term


# User("name",name = "Komil" , age = 28 , birthday='2000-01-01').insert()
# User(age = 25).update(id = 3)
# for i in User().users_object(id = 3):
#     print(i.name)
