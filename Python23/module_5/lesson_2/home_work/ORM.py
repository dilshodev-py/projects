# Object Relation Mapping
import json

import psycopg2
from pydantic.dataclasses import dataclass




class DB:
    connection = psycopg2.connect(
        dbname="tg_db",
        user="postgres",
        host="localhost",
        port=5432,
        password=1
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


class Member(DB):
    def __init__(self,*param ,
                 user_id = None,
                 first_name = None,
                 last_name = None,
                 username = None,
                 location = None):
        self.param = param
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location

# lat = 1234543
# long = 1234323
# location = {"longitude" : long , "latitude" : lat}
# loc_json = json.loads(location)

# Member(user_id=12345 , first_name='Botir' , last_name="Qodirov" , username="botir" , location=loc_json).insert()

class Document(DB):
    def __init__(self , *param  , owner_id= None , file_id = None , type = None):
        self.param = param
        self.owner_id = owner_id
        self.file_id = file_id
        self.type = type






# Member(user_id=1 , first_name="JOhn" , last_name="Doe" , username="username").insert()
# print(Member().select(user_id = 1))











