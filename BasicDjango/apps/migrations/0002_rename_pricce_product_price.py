# Generated by Django 5.0.6 on 2024-06-21 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pricce',
            new_name='price',
        ),
    ]
