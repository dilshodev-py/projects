from django.db.models import Model, CharField


class Mosque(Model):
    name = CharField(max_length=255)
