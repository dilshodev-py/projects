from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, Model, ForeignKey, CASCADE, DateTimeField, TextField, IntegerField, \
    FloatField, TextChoices, SET_NULL
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _

class BaseModel(Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    phone_number = CharField(max_length=14)
    photo = ImageField(upload_to='users/')


class Category(BaseModel, MPTTModel):
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')

    name = CharField(verbose_name=_('name'), max_length=255)
    image = ImageField(upload_to='categories/')

    class MPTTMeta:
        level_attr = 'mptt_level'

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=255)
    description = TextField()
    quantity = IntegerField(default=1)
    price = FloatField()
    category = ForeignKey('apps.Category', CASCADE, related_name='products')

    class Meta:
        ordering = ['-created_at']

    @property
    def first_image(self):
        return self.images.first()


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')


class Order(BaseModel):
    class Status(TextChoices):
        PENDING = 'pending', 'Pending'
        PROCESSING = 'processing', 'Processing'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'

    user = ForeignKey('apps.User', CASCADE, related_name='orders')
    product = ForeignKey('apps.Product', CASCADE, related_name='order_items')
    stream = ForeignKey('apps.Stream', SET_NULL, related_name='orders', null=True)
    status = CharField(max_length=255, choices=Status.choices, default=Status.PENDING)


class Stream(BaseModel):
    user = ForeignKey('apps.User', CASCADE, related_name='streams')
    product = ForeignKey('apps.Product', CASCADE, related_name='products')


class NewProduct(Model):
    name = CharField(max_length=255)