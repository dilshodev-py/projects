from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db.models import CASCADE, Model, ForeignKey, BooleanField
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import CharField , IntegerField , TextField
from parler.models import TranslatableModel


class User(AbstractUser):
    age = IntegerField("age", null=True)




class Category(MPTTModel, TranslatableModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self',CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return f"{self.name}"


class Product(Model):
    name = CharField(max_length=50)
    price = IntegerField()
    description = TextField(null=True ,blank=True)
    is_premium = BooleanField(default=0)
    is_new = BooleanField(default=0)
    category = ForeignKey('app.Category' , CASCADE)

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produktlar'

    def __str__(self):
        return f"{self.name}"
