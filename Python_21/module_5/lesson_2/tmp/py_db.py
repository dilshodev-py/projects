# # psycopg2-binary
# # psycopg2
# import psycopg2
# con = psycopg2.connect(
#     dbname = "tg_db",
#     user = "postgres",
#     password = "1",
#     host = "localhost",
#     port = "5432"
# )
# cur = con.cursor()
# query1 = 'select * from users'
# query2 = '''insert into users (fullname , phone_number, username , photo , bio)
# values (%s , %s , %s , %s , %s)'''
# params2 = ("Botir QOdirov" , "+998993583231" , "botir" , "😈" , "nimadir")
# cur.execute(query2 , params2)
# con.commit()

import psycopg2


class DB:
    con = psycopg2.connect(
        database="tg_db",
        user="postgres",
        password="1",
        host="localhost",
        port=5432)

    cur = con.cursor()

    def insert(self):
        attribute = self.__dict__
        del attribute["param"]
        table_name = self.__class__.__name__.lower() + "s"
        columns_name = " , ".join(attribute.keys())
        params = tuple(attribute.values())
        formats = " , ".join(['%s'] * len(columns_name.split(',')))
        query = f"""
            insert into {table_name} ({columns_name})
            values ({formats})
        """
        self.cur.execute(query, params)
        self.con.commit()

    def update(self, **conditions):
        class_self = dict(self.__dict__)
        del class_self['param']
        table_name = self.__class__.__name__.lower() + "s"
        set_field = " = %s , ".join([k for k, v in class_self.items() if not v is None]) + " = %s"
        cond = " = %s and ".join(conditions.keys()) + " = %s"
        params = [i for i in class_self.values() if not i is None] + list(conditions.values())
        query = f"""
            update {table_name} set {set_field} where {cond}
        """
        self.cur.execute(query, params)
        self.con.commit()

    def delete(self, **conditions):
        cond = " = %s and ".join(conditions.keys()) + " = %s"
        params = tuple(conditions.values())
        table_name = self.__class__.__name__.lower() + "s"

        query = f"""
            delete from {table_name} where {cond};
        """
        self.cur.execute(query, params)
        self.con.commit()

    def select(self, **conditions):
        table_name = self.__class__.__name__.lower() + "s"
        columns = "*" if not self.param else " , ".join(self.param)
        condition = "where " + " = %s and ".join(conditions.keys()) + " = %s" if conditions else ''
        params = tuple(conditions.values())
        query = f"""
            select {columns} from {table_name} {condition}
        """
        self.cur.execute(query, params)
        data = self.cur.fetchall()
        return data


class User(DB):
    def __init__(self, *param,
                 fullname: str = None,
                 phone_number: str = None,
                 username: str = None,
                 photo: str = None,
                 bio: str = None):
        self.param = param
        self.fullname = fullname
        self.phone_number = phone_number
        self.username = username
        self.photo = photo
        self.bio = bio


user = User(fullname ="Muhtor Kamolov" ,
            phone_number="+998991234567" ,
            username="Muhtor" , photo=":)" ,
            bio="Nexia Legenda")
user.insert()
