import json
from abc import ABC, abstractmethod
from apps.utils import send_email


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(f"/home/dilshod/PycharmProjects/OnlineShop/DB/{self.file_name}", 'r') as f:
            data = json.load(f)
        return data

    def write(self, data):
        with open(f"/home/dilshod/PycharmProjects/OnlineShop/DB/{self.file_name}", 'w') as f:
            json.dump(data, f, indent=3)


class ModelAbstract(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, field, new_value):
        pass


class User(ModelAbstract):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 email: str = None,
                 password: str = None,
                 role: str = "USER",
                 join_at: str = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.join_at = join_at

    def update(self, field, new_value):
        users: dict = self.get_all()
        for id, user in users.items():
            if id == str(self.id):
                users[id][field] = new_value
        File("users.json").write(users)

    def give_admin(self):
        file = File("users.json")
        users = file.read()
        for id, user in users.items():
            if user.get("email") == self.email:
                users[id]["role"] = 'ADMIN'
                break
        else:
            raise Exception("Bunday email topilmadi !")
        file.write(users)

    def is_valid(self):
        file = File('users.json')
        users: list = list(file.read().values())
        if not "@" in self.email:
            raise Exception("Email da xatolik")
        for user in users:
            if user.get('email') == self.email:
                raise Exception("Bunday email ro'yhatdan o'tgan !")

        if len(self.password) < 4:
            raise Exception("Password 4 dan kotta emas !")

        code = send_email(self.email)
        return code

    def is_login(self):
        file = File('users.json')
        users = file.read().values()
        for user in users:
            if user.get('email') == self.email and user.get('password') == self.password:
                return user
        raise Exception("Bunday account mavjud emas")

    def sequence_id(self):
        file = File('users.json')
        users: list = list(file.read().keys())
        if users:
            return int(users[-1]) + 1
        return 1

    def save(self) -> None:
        file = File('users.json')
        user = {self.id: self.__dict__}
        users: dict = file.read()
        users.update(user)
        # users[self.id] = self.__dict__
        file.write(users)

    def delete(self) -> None:
        file = File('users.json')
        users: dict = file.read()
        del users[str(self.id)]
        file.write(users)

    def get(self) -> dict:
        file = File('users.json')
        users: dict = file.read()
        user: dict = users.get(str(self.id))
        return user

    def get_all(self) -> dict:
        file = File('users.json')
        users: dict = file.read()
        return users


class Category(ModelAbstract):
    def __init__(self,
                 id: int = None,
                 name: str = None):

        self.id = id
        self.name = name

    def update(self , field , new_value):
        categories: dict = self.get_all()
        for id, category in categories.items():
            if id == str(self.id):
                categories[id][field] = new_value
        File("categories.json").write(categories)
    def save(self) -> None:
        file = File('categories.json')
        category = {self.id: self.__dict__}
        categories: dict = file.read()
        categories.update(category)
        file.write(categories)

    def delete(self) -> None:
        file = File('categories.json')
        categories: dict = file.read()
        del categories[str(self.id)]
        file.write(categories)

    def get(self) -> dict:
        file = File('categories.json')
        categories: dict = file.read()
        category: dict = categories.get(str(self.id))
        return category

    def get_all(self) -> dict:
        file = File('categories.json')
        categories: dict = file.read()
        return categories

    def sequence_id(self): # noqa
        file = File('categories.json')
        categories: list = list(file.read().keys())
        if categories:
            return int(categories[-1]) + 1
        return 1


class Product(ModelAbstract):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 amount: int = None,
                 description: str = None,
                 price: int = None,
                 is_active: str = "PROCESS",
                 category_id: int = None
                 ):
        self.id = id
        self.name = name
        self.amount = amount
        self.description = description
        self.price = price
        self.is_active = is_active
        self.category_id = category_id

    def update(self, field, new_value):
        products: dict = self.get_all()
        for id, product in products.items():
            if id == str(self.id):
                products[id][field] = new_value
        File("products.json").write(products)

    def save(self) -> None:
        file = File('products.json')
        product = {self.id: self.__dict__}
        products: dict = file.read()
        products.update(product)
        file.write(products)

    def delete(self) -> None:
        file = File('products.json')
        products: dict = file.read()
        del products[str(self.id)]
        file.write(products)

    def get(self) -> dict:
        file = File('products.json')
        products: dict = file.read()
        product: dict = products.get(str(self.id))
        return product

    def get_all(self) -> dict:
        file = File('products.json')
        products: dict = file.read()
        return products

    def process_product(self):
        products: dict = self.get_all()
        result = []
        for product in products.values():
            if product.get("is_active") == "PROCESS":
                result.append(product)
        return result
