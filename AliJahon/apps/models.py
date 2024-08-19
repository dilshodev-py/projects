import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, DateTimeField, ForeignKey, CASCADE, CharField, IntegerField, TextField, SlugField, \
    FloatField, TextChoices, ImageField, Manager, SET_NULL
from django.utils.functional import cached_property
from django.utils.text import slugify


class BaseModel(Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseSlugModel(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = "admin", 'Admin'
        OPERATOR = "operator", 'Operator'
        MANAGER = "manager", 'Manager'
        DRIVER = "driver", 'Driver'
        USER = "user", 'User'

    username = None
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    phone_number = CharField(max_length=50, null=False, unique=True)  # TODO add phone validator and remove username
    role = CharField(max_length=20, choices=Role.choices, default=Role.USER)
    district = ForeignKey('apps.District', CASCADE, null=True, blank=True)
    region = ForeignKey('apps.Region', CASCADE, null=True, blank=True)

    @cached_property
    def wishlist_count(self):
        return self.wishlists.count()

    @property
    def is_operator(self):
        return self.role == self.Role.OPERATOR

    @cached_property
    def wishlists_all(self):
        return self.wishlists.values_list('product_id', flat=True)


class Category(BaseSlugModel):
    image = ImageField(upload_to='category/')
    icon = CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Product(BaseSlugModel):
    description = TextField()
    price = FloatField()
    shipping_cost = FloatField()
    count = IntegerField()
    category = ForeignKey('apps.Category', CASCADE, to_field='slug', related_name='products')

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Products'

    @property
    def first_image(self):
        return self.product_images.first()

    @property
    def is_new(self):
        return (datetime.datetime.fromisoformat('2024-03-26') - datetime.datetime.now()).days <= 7


class WishList(BaseModel):
    user = ForeignKey('apps.User', CASCADE, related_name='wishlists')
    product = ForeignKey('apps.Product', CASCADE, related_name='wishlists')

    class Meta:
        ordering = ['-created_at']


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', CASCADE, to_field='slug', related_name='product_images')


class Order(BaseModel):
    class Status(TextChoices):
        NEW = "new", 'New'
        READY_TO_START = "ready_to_start", 'Ready To Start'
        BEING_DELIVERED = "being_delivered", 'Being Delivered'
        THEN_TAKES = "then_takes", 'Then Takes'
        HOLD = "hold", 'Hold'
        FAILED_ABORTED = "failed_aborted", 'Failed Aborted'
        DELIVERED = "delivered", 'Delivered'
        NOT_PICK_UP_PHONE = 'not_pick_up_phone', 'Not pick up phone'
        CANCELED = 'canceled', 'Canceled'
        ARCHIVED = 'archived', 'Archived'

    product = ForeignKey('apps.Product', CASCADE, to_field='slug', related_name='orders')
    name = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    count = IntegerField(default=1)
    comment = TextField(null=True)
    amount_price = FloatField(default=0)
    status = CharField(max_length=50, choices=Status.choices, default=Status.NEW)
    user = ForeignKey('apps.User', CASCADE, related_name='orders')
    stream = ForeignKey('apps.Stream', CASCADE, null=True, blank=True, verbose_name='oqim', related_name='orders')
    district = ForeignKey('apps.District', SET_NULL, null=True, related_name="orders")

    def __str__(self):
        return self.name




class Stream(BaseModel):
    name = CharField(max_length=255)
    count = IntegerField(default=0)
    product = ForeignKey('apps.Product', CASCADE, related_name='streams')
    user = ForeignKey('apps.User', CASCADE, related_name='streams')

    class Meta:
        ordering = '-created_at',


class SiteSettings(Model):
    delivery_price = FloatField(default=0)




class Region(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', CASCADE, related_name='districts')

    def __str__(self):
        return self.name
