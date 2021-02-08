from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator
from django.contrib.auth.models import User


class Cliente (models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField()
    #fecha_nacimiento= models.DateField()
    direccion = models.CharField(max_length=200)
    cod_postal = models.CharField(max_length=5, validators=[RegexValidator(r'^[0-9]{5}$')])

class Articulo(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock_maximo = models.IntegerField()
    stock_actual = models.IntegerField()

class Reparto (models.Model):
    nombre = models.CharField(max_length=64)
    identificador=models.CharField(max_length=64)
    dia= models.DateField()

POSIBLES_ESTADOS = [
    ('no asignado', 'no asignado'),
    ('en reparto', 'en reparto'),
    ('incidencia', 'incidencia'),
    ('repartido', 'repartido')
]

class Pedido (models.Model):
    estado = models.CharField(max_length=50, choices=POSIBLES_ESTADOS)
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    reparto = models.ForeignKey(Reparto, on_delete=models.CASCADE)


    


