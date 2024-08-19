import os

from db.config import Config
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DB(Config):
    connect = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER")
    )
    cur = connect.cursor()

    def insert(self):
        """
        insert into table_name(field1 , field2) values (%s , %s);
        """
        fields = " , ".join(self.kwargs.keys())
        s = " , ".join(["%s"] * len(self.kwargs.keys()))
        query = f"""insert into {self.__class__.__name__.lower()} ({fields}) values ({s});"""
        params = tuple(self.kwargs.values())

        self.cur.execute(query, params)
        self.connect.commit()

    def delete(self):
        if not self.kwargs.keys():
            raise Exception("xatolik !")
        cond = "= %s and ".join(self.kwargs.keys()) + "= %s"
        query = f"""
            delete from {self.__class__.__name__.lower()} where {cond} 
        """
        params = tuple(self.kwargs.values())

        self.cur.execute(query, params)
        self.connect.commit()

    def update(self, **set_value):

        set = "= %s and ".join(set_value.keys()) + "= %s"
        cond = "= %s and ".join(self.kwargs.keys()) + "= %s"
        params = tuple(list(set_value.values()) + list(self.kwargs.values()))
        query = f"""
        update {self.__class__.__name__.lower()} set {set} where {cond}
        """
        self.cur.execute(query, params)
        self.connect.commit()

    def select(self, *fields):
        if not fields:
            fields = "*"
        else:
            fields = " , ".join(fields)

        cond = ""
        if self.kwargs.keys():
            cond = "where " + "= %s and ".join(self.kwargs.keys()) + "= %s"

        params = tuple(self.kwargs.values())
        query = f"""select {fields} from {self.__class__.__name__.lower()} {cond}"""
        self.cur.execute(query, params)
        return self.cur.fetchall()
