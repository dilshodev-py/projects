from django.db.models import CharField, TextField, DecimalField, ImageField, Model, ForeignKey, CASCADE


class Category(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=100)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    image = ImageField(upload_to='products/')
    category = ForeignKey('apps.Category' , on_delete= CASCADE , related_name='products')
    def __str__(self):
        return self.name