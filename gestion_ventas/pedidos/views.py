from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Cliente, Pedido, Articulo, Reparto
import datetime, time
from django.core import serializers

# Create your views here.
# pylint: disable=E1101

#def welcome_page(request):
#    return render (request, "usuarios/welcome.html")


def index(request):
    return render(request, "pedidos/index.html")

def cliente(request):
    return render(request, "pedidos/cliente.html")

def personal(request):
    return render(request, "pedidos/personal.html")