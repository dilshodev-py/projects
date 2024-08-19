from os import getenv
from dotenv import load_dotenv
import psycopg2
load_dotenv()

# I18n

class DB:
    connection = psycopg2.connect(
        dbname=getenv('DB_NAME'),
        user=getenv('DB_USER'),
        host=getenv('HOST'),
        port=getenv('PORT'),
        password=getenv('PASSWORD')
    )
    cursor = connection.cursor()

    def insert(self):
        self_dict = self.__dict__
        del self_dict['param']
        table_name = self.__class__.__name__.lower() + "s"
        col_name = " , ".join(self_dict.keys())
        format = " , ".join(["%s"] * len(self_dict.values()))
        params = tuple(self_dict.values())
        query = f"insert into {table_name} ({col_name}) values ({format})"
        self.cursor.execute(query, params)
        self.connection.commit()

    def select(self, **conditions):
        condition = ""
        if conditions:
            condition = "where " + " = %s and ".join(conditions.keys()) + " = %s"

        if not self.param:
            field = "*"
        else:
            field = " , ".join(self.param)
        params = tuple(conditions.values())
        table_name = self.__class__.__name__.lower() + "s"
        query = f"select {field} from {table_name} {condition}"
        self.cursor.execute(query, params)
        data = self.cursor.fetchall()
        return data

    def update(self, **conditions):
        conditions_format = ""
        if conditions:
            conditions_format = "where " + " = %s and ".join(conditions.keys()) + " = %s"
        self_dict = self.__dict__
        del self_dict['param']
        table_name = self.__class__.__name__.lower() + "s"
        keys = [k for k , v in self_dict.items() if not v is None]
        params = [v for k , v in self_dict.items() if not v is None]
        params.extend(conditions.values())
        set_format = " = %s , ".join(keys) + " = %s"
        query = f"""update {table_name} set {set_format} {conditions_format} """
        self.cursor.execute(query , tuple(params))
        self.connection.commit()

    def delete(self, **conditions):
        if conditions:
            condition_format = "where " + " = %s and ".join(conditions.keys()) + " = %s"
        params = tuple(conditions.values())
        table_name = self.__class__.__name__.lower() + "s"
        query = f"""delete from {table_name} {condition_format}"""
        self.cursor.execute(query , params)
        self.connection.commit()







