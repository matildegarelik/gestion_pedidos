# Generated by Django 3.1.2 on 2021-02-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20210208_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('no asignado', 'no asignado'), ('en reparto', 'en reparto'), ('incidencia', 'incidencia'), ('repartido', 'repartido'), ('preparado', 'preparado')], max_length=50),
        ),
    ]
