import psycopg2

# pip install psycopg2-binary

DB_CONFIG = {
    "dbname": "tg_db",
    "user": "postgres",
    "password": "1",
    "host": "localhost",
    "port": 5432
}


class DB:
    con = psycopg2.connect(**DB_CONFIG)
    cur = con.cursor()

    def delete(self, **cond):
        table_name = f"{self.__class__.__name__.lower()}s"
        cond_format = " = %s and ".join(cond.keys()) + " = %s"
        cond_param = tuple(cond.values())
        query = f"""delete from {table_name} where {cond_format} CASCADE """
        self.cur.execute(query, cond_param)
        self.con.commit()

    def update(self, **cond):
        table_name = self.__class__.__name__.lower() + "s"
        set_format = " = %s , ".join(self.kwargs.keys()) + " = %s"
        set_params = tuple(self.kwargs.values())
        cond_format = " = %s and ".join(cond.keys()) + " = %s"
        cond_param = tuple(cond.values())
        params = set_params + cond_param
        query = f"""
        update {table_name} set {set_format} where {cond_format}
        """
        self.cur.execute(query, params)
        self.con.commit()

    def all(self):
        table_name = f"{self.__class__.__name__.lower()}s"
        fields = " , ".join(self.args) if self.args else "*"  # "id , name"

        query = f"""
            select {fields} from {table_name};
        """
        self.cur.execute(query)
        data = self.cur.fetchall()
        return data

    def filter(self, **cond):
        fields = " , ".join(self.args) if self.args else "*"# id , name
        table_name = self.__class__.__name__.lower() + "s"
        params = tuple(cond.values())
        cond = " = %s and ".join(cond.keys()) + '= %s'
        query = f"""
            select {fields} from {table_name} where {cond}
        """
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def save(self):
        table_name = self.__class__.__name__.lower() + "s"
        fields = " , ".join(self.kwargs.keys())  #
        values = " , ".join(["%s"] * len(self.kwargs))
        params = tuple(self.kwargs.values())
        query = f"""
            insert into {table_name} ({fields})
            values ({values})
        """
        try:
            self.cur.execute("begin;")
            self.cur.execute(query, params)
            self.cur.execute(query, params)
            self.cur.execute(query, params)
            self.cur.execute(query, params)
            self.con.commit()
        except Exception:
            self.con.rollback()

        self.con.commit()
