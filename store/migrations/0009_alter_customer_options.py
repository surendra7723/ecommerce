# Generated by Django 3.2.4 on 2024-07-07 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_ph4one_customer_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
