# from django.forms import CharField, EmailField, ModelForm, ImageField
#
# from apps.models import User
#
#
# class UserModelForm(ModelForm):
#     first_name = CharField(label='First Name', max_length=100)
#     last_name = CharField(label='Last Name', max_length=100)
#     phone_number = CharField(label='Phone Number', max_length=100)
#     email = EmailField(label='Your Email')
#     photo = ImageField(required=False)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'phone_number', 'email', 'photo']
#
#     def clean(self):
#         data = self.cleaned_data
#         phone_number = data.get("phone_number")
#         if User.objects.filter(first_name=phone_number).exists():
#             self.add_error("phone_number", f"\"{phone_number}\" is already in use. Please pick another phone_number.")
#         return data
