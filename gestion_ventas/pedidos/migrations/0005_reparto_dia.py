# Generated by Django 3.1.2 on 2021-02-08 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_remove_reparto_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparto',
            name='dia',
            field=models.DateField(default=datetime.date(2021, 2, 8)),
        ),
    ]
