from django.forms import ModelForm, CharField, EmailField, ImageField, IntegerField, ModelChoiceField

from apps.models import Product
from apps.models.users import User, Stream


class StreamForm(ModelForm):
    product = ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Stream
        fields = ['name', 'product']


class UserModelForm(ModelForm):
    first_name = CharField(label='First Name', max_length=100)
    last_name = CharField(label='Last Name', max_length=100)
    phone_number = CharField(label='Phone Number', max_length=100)
    email = EmailField(label='Your Email')
    photo = ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'photo']
