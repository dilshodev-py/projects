import re

from django.forms import ModelForm, CharField, EmailField, ImageField, Form, ModelChoiceField, ModelMultipleChoiceField

from apps.models import User, Order, Product, Stream, Category, Region, District


class LoginForm(Form):
    phone_number = CharField(max_length=255)
    password = CharField(max_length=255)


class RegisterForm(Form):
    first_name = CharField(max_length=255)
    phone_number = CharField(max_length=255)
    password = CharField(max_length=255)


class UserModelForm(ModelForm):
    first_name = CharField(label='First Name', max_length=100)
    last_name = CharField(label='Last Name', max_length=100)
    phone_number = CharField(label='Phone Number', max_length=100)
    email = EmailField(label='Your Email')
    photo = ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'photo', 'region', 'district']


class OrderModelForm(ModelForm):
    product = ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = ['name', 'phone_number' , 'product']

    def clean_phone_number(self):
        return re.sub(r'\D', '', self.cleaned_data.get('phone_number'))


class StreamForm(ModelForm):
    product = ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Stream
        fields = ['name', 'product']
