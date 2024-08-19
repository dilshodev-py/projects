# Object Relation Mapping
import psycopg2
from pydantic.dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    name: str
    age: int
    phone_number: str


@dataclass
class ProductDTO:
    id: int
    name: str
    count: int


class DB:
    connection = psycopg2.connect(
        dbname="postgres",
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
    def __init__(self, *param, user_id = None, first_name = None, last_name = None, username = None):
        self.param = param
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username


print(Member().select())









# User(name = "Botir" , age = 25 , phone_number = "+998993573231").insert()


class Product(DB):
    def __init__(self,*param , name = None, count=None):
        self.param = param
        self.name = name
        self.count = count

# products = Product(name = "Iphone 15" , count=50).insert()
# products = Product(name = "Iphone 15", count=1).insert()
products = Product().delete(id = 2)

# products_obj : list[ProductDTO] = []
# for product  in products:
#     products_obj.append(ProductDTO(*product))
# print(products_obj[0].name)
