from django.contrib import admin
from django.urls import path, include
from . import views

app_name= "pedidos"
urlpatterns = [
    path("", views.index, name='index'),
    path("cliente/", views.cliente, name="cliente"),
    path("personal/", views.personal, name="personal"),
]
