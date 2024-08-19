from django.db import models
from django.db.models import Model, CharField, IntegerField, DateField, TextChoices, ForeignKey, CASCADE
from django.forms import Widget


class Task(Model):
    name = CharField(max_length=100)
    progress = IntegerField()
    due_date = DateField()

    def __str__(self):
        return self.name


class Company(Model):
    name = CharField(max_length=100)
    address = CharField(max_length=100)

    def __str__(self):
        return self.name


class Vacancy(Model):
    class Type(TextChoices):
        FULL_TIME = 'full_time', 'Full time'
        REMOTE = 'remote', 'Remote'
        CONTRACT = 'contract', 'Contract'
        WFH = 'wfh', 'Wfh'

    class Meta:
        ordering = '-name',

    name = CharField(max_length=100, verbose_name='namee')
    type = CharField(max_length=50, choices=Type.choices, default=Type.FULL_TIME)
    company = ForeignKey('apps.Company', CASCADE, related_name='vacancies', blank=True, null=True)

    def __str__(self):
        return self.name
