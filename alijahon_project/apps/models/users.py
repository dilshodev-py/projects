import datetime

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, FloatField, IntegerField, TextField, \
    ForeignKey, CASCADE, SlugField, TextChoices
from django.utils.functional import cached_property
from django.utils.text import slugify

from apps.models.base import BaseModel


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = "admin", 'Admin'
        OPERATOR = "operator", 'Operator'
        MANAGER = "manager", 'Manager'
        DRIVER = "driver", 'Driver'
        USER = "user", 'User'

    phone_number = CharField(max_length=50, null=False)
    role = CharField(max_length=20, choices=Role.choices, default=Role.USER)

    @cached_property
    def wishlist_count(self):
        return self.wishlists.count()

    @property
    def is_operator(self):
        return self.role == self.Role.OPERATOR
    # @property
    # def order_by(self):
    #     self.orders


class Category(BaseModel):
    name = CharField(max_length=255)
    image = ImageField(upload_to='category/')
    icon = CharField(max_length=255, blank=True, null=True)
    slug = SlugField(unique=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.name}"


class Product(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)
    description = TextField()
    price = FloatField()
    shipping_cost = FloatField()
    count = IntegerField()
    category = ForeignKey('apps.Category', CASCADE, to_field='slug', related_name='products')

    class Meta:
        ordering = ['-created_at']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    @property
    def first_image(self):
        return self.product_images.first()

    @property
    def is_new(self):
        return (datetime.datetime.fromisoformat('2024-03-26') - datetime.datetime.now()).days <= 7

    def __str__(self):
        return self.name

class WishList(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='wishlists')
    product = ForeignKey('apps.Product', CASCADE, related_name='wishlists')


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product',CASCADE, to_field='slug', related_name='product_images')


class Order(BaseModel):
    class Status(TextChoices):
        NEW = "new", 'New'
        READY_TO_START = "ready_to_start", 'Ready To Start'
        BEING_DELIVERED = "being_delivered", 'Being Delivered'
        DELIVERED = "delivered", 'Delivered'
        NOT_PICK_UP_PHONE = 'not_pick_up_phone', 'Not pick up phone'
        CANCELED = 'canceled', 'Canceled'

    product = ForeignKey('Product', CASCADE, related_name='orders')
    user = ForeignKey('User', CASCADE, related_name='orders')
    status = CharField(max_length=50, choices=Status.choices, default=Status.NEW)
    stream = ForeignKey('Stream', CASCADE , null=True , blank=True , verbose_name='oqim', related_name='orders')


class Stream(BaseModel):
    name = CharField(max_length=255)
    count = IntegerField(default=0)
    product = ForeignKey('Product', CASCADE, related_name='streams')
    user = ForeignKey('User', CASCADE, related_name='streams')
