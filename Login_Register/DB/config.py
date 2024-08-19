import psycopg2


class DB:
    connect = psycopg2.connect(
        dbname="lesson_4",
        user="postgres",
        password=1,
        host='127.0.0.1',  # localhost
        port=5432
    )

    cur = connect.cursor()


class DDL(DB):
    def __init__(self, table_name, **kwargs):
        self.table_name = table_name
        self.fields = kwargs

    def create(self):
        field = ""
        for col, type in self.fields.items():
            field += f"{col} {type},\n"
        field = field.strip('\n,')
        #
        query = f"""
        create table if not exists {self.table_name} ({field});
        """
        self.cur.execute(query)
        self.connect.commit()

    def drop(self):
        query = f"""drop table {self.table_name};"""
        self.cur.execute(query)
        self.connect.commit()

    def truncate(self):
        query = f"""truncate table {self.table_name};"""
        self.cur.execute(query)
        self.connect.commit()

    def alter(self, mode, value=''):
        query = f"""alter table {self.table_name} {mode} {value}"""
        self.cur.execute(query)
        self.connect.commit()


class DML(DB):

    def insert(self):

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


user_table = DDL("users" ,
                 id = "serial primary key",
                 username = "varchar(255) unique not null",
                 password = "varchar(8)")

user_table.create()
