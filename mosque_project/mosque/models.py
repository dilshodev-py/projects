from django.db.models import (Model, CharField, ForeignKey, SET_NULL, TextChoices, DecimalField,
                              DateTimeField, IntegerField)


class BaseModel(Model):
    created_at = DateTimeField(auto_now=True , null=True)

    class Meta:
        abstract = True


class Mosque(BaseModel):
    name = CharField(verbose_name='Nomi', max_length=255)
    address = CharField(verbose_name='Manzili', max_length=255)
    account_number = CharField(verbose_name='Hisob raqami', max_length=20)
    bank = CharField(verbose_name='Bank', max_length=255)
    bank_code = IntegerField('Bank kodi')
    stir = IntegerField('СТИР')

    class Meta:
        verbose_name = 'Masjid'
        verbose_name_plural = 'Masjidlar'

    def __str__(self):
        return self.name


class TransactionType(Model):
    class Type(TextChoices):
        INCOME = 'income', 'Kirim'
        OUTCOME = 'outcome', 'Chiqim'

    name = CharField('Nomi', max_length=255)
    income = CharField('Turi', max_length=25, choices=Type.choices)

    class Meta:
        verbose_name = "Pul o'tkazma turi"
        verbose_name_plural = "Pul o'tkazma turlari"

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    count = IntegerField("Soni", default=1)
    amount = DecimalField('Pul miqdori', max_digits=10, decimal_places=0)
    type = ForeignKey('mosque.TransactionType', SET_NULL, null=True, verbose_name="O'tkazma turi",
                      related_name='transactions')
    mosque = ForeignKey('mosque.Mosque', SET_NULL, null=True, verbose_name="Masjid", related_name='transactions')

    class Meta:
        verbose_name = "Pul o'tkazma"
        verbose_name_plural = "Pul o'tkazmalari"

    def __str__(self):
        return f"{self.mosque.name}"
