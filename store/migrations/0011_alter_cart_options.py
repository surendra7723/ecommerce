# Generated by Django 4.2.14 on 2024-07-14 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20240710_0714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['created_at']},
        ),
    ]
