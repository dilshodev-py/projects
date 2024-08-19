import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from os.path import join
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = join(BASE_DIR, 'db')


@dataclass
class DbManager:
    @property
    def objects(self):
        file_name = self.__class__.__name__.lower() + "s.json"
        with open(join(DB_PATH, file_name), 'r') as f:
            data = json.load(f)
        for i, d in enumerate(data):
            data[i] = self.__class__(**d)  # noqa
        return data

    def write(self, data: list[objects]):
        file_name = self.__class__.__name__.lower() + "s.json"
        res = [i.__dict__ for i in data]
        with open(join(DB_PATH, file_name), 'w') as f:
            json.dump(res, f, indent=3)


@dataclass
class CRUD(DbManager):

    def create(self):
        objects = self.objects
        self.id = objects[-1].id + 1 if objects else 1
        objects.append(self)
        self.write(objects)

    def update(self, **fields):
        objects = self.objects
        for obj in objects:
            if obj.id == self.id:
                for k, v in fields.items():
                    setattr(obj, k, v)
                self.write(objects)
                break

    def delete(self):
        objects = self.objects
        for obj in objects:
            if obj.id == self.id:
                objects.remove(obj)
                self.write(objects)
                break

    def read(self):
        objects = self.objects
        for obj in objects:
            if obj.id == self.id:
                return obj


@dataclass
class Category(CRUD):  # noqa
    id: int = None
    name: str = None


@dataclass
class Brand(CRUD):  # noqa
    id: int = None
    name: str = None


@dataclass
class Meta(CRUD):  # noqa
    id: int = None
    barcode: str = None
    qr_code: str = None
    created_at: str = str(datetime.now())[:-7]
    updated_at: str = None


@dataclass
class ProductImage(CRUD):  # noqa
    id: int = None
    image_url: str = None
    product_id: int = None


@dataclass
class User(CRUD):  # noqa
    id: int = None
    name: str = None
    email: str = None


@dataclass
class CommentRating(CRUD):
    user_id: int = None
    comment_id: int = None


@dataclass
class ProductRating(CRUD):
    user_id: int = None
    product_id: int = None


@dataclass
class Comment(CRUD):  # noqa
    id: int = None
    rating: int = 0
    message: str = None
    created_at: str = str(datetime.now())
    user_id: int = None
    product_id: int = None


class WeightType(Enum):
    kg = 1
    pound = 2
    netto = 3


@dataclass
class Product(CRUD):  # noqa
    id: int = None
    title: str = None
    description: str = None
    price: float = None
    discount_percentage: float = None
    rating: float = None
    stock: int = None
    sku: str = None
    weight: float = None
    weight_type: int = None
    dimensions: dict[str, float] = None
    warranty_information: str = None
    availability_status: str = None
    shipping_information: str = None
    minimum_order_quantity: int = None
    return_policy: str = None
    thumbnail: str = None
    category_id: int = None
    brand_id: int = None
    meta_id: int = None