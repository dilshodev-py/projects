from django.contrib.auth.models import AbstractUser
from django.db.models import (Model, CharField, ForeignKey, SET_NULL, TextChoices, DateField, DecimalField, ImageField,
                              FileField, IntegerField)


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Hodim'

    first_name = CharField("Ismi", max_length=150, blank=True)
    last_name = CharField("Familyasi", max_length=150, blank=True)
    birthday = DateField("Tug'ilgan kuni", null=True)
    mosque = ForeignKey('mosque.Mosque', SET_NULL, null=True, blank=True, verbose_name="Masjid", related_name='users')
    role = ForeignKey('apps.UserRole', SET_NULL, null=True, blank=True, verbose_name="Vazifasi", related_name='users')
    salary = DecimalField('Oylik', max_digits=10, decimal_places=2, null=True)
    type = CharField(max_length=25, choices=Type.choices, default=Type.STAFF)
    command_file = FileField('Buyruq fayli',upload_to='user/commands_file/', null=True)
    passport_number = IntegerField('passportning 14 talik raqami',null=True)

    class Meta:
        verbose_name = 'Hodim'
        verbose_name_plural = 'Hodimlar'


class UserStaffProxy(User):
    class Meta:
        proxy = True
        app_label = 'mosque'
        verbose_name = 'Hodim'
        verbose_name_plural = 'Hodimlar'


class UserRole(Model):
    name = CharField("Vazifasi", max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lavozim'
        verbose_name_plural = 'Lavozimlar'
