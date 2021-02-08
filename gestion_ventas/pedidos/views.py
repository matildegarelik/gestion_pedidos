from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Cliente, Pedido, Articulo, Reparto
import datetime, time
from django.core import serializers
from operator import itemgetter


# Create your views here.
# pylint: disable=E1101

#def welcome_page(request):
#    return render (request, "usuarios/welcome.html")


def index(request):
    return render(request, "pedidos/index.html")

def cliente(request):
    #clientes =  Cliente.objects.all()
    if request.method=="POST":
        if request.POST['submit']=="Registrarse":
            if Cliente.objects.filter(email=request.POST['email']).count() > 0:
                return render(request, "pedidos/cliente.html", {
                    'mensaje': 'Ya existe un registro con esa  dirección de correo electrónico' 
                })
            else:
                nuevo_cliente = Cliente(
                    nombre= request.POST['nombre'],
                    apellido= request.POST['apellido'],
                    email= request.POST['email'],
                    edad= request.POST['edad'],
                    direccion= request.POST['direccion'],
                    cod_postal= request.POST['cp'],
                )
                nuevo_cliente.save()
                return render(request, "pedidos/cliente.html", {
                    'mensaje': 'Registrado con éxito! Ya puede acceder con su email.',
                    'accion': '1'
                })
        elif request.POST['submit']=="Ingresar":
            if Cliente.objects.filter(email=request.POST['email']).count() > 0:
                return render(request, "pedidos/cliente.html", {
                    'mensaje': 'Logueado con éxito!',
                    'cliente_logueado': Cliente.objects.get(email=request.POST['email']),
                    'articulos': Articulo.objects.all(),
                    'accion': '2'
                })
            else:
                return render (request, "pedidos/cliente.html", {
                    'mensaje': 'El email ingresado no figura en nuestros registros.',
                })
        elif request.POST['submit']== "Comprar":
            nuevo_pedido = Pedido(
                estado="no asignado",
                cantidad = request.POST['cantidad'],
                articulo= Articulo.objects.get(id=request.POST['id-articulo']),
                cliente= Cliente.objects.get (id=request.POST['id-cliente'])
            )
            nuevo_pedido.save()
            return render(request, "pedidos/cliente.html", {
                    'mensaje': 'Compra realizada con éxito!',
                    'cliente_logueado': Cliente.objects.get(id=request.POST['id-cliente']),
                    'articulos': Articulo.objects.all(),
                    'accion': '2'
                })

    else:
        return render(request, "pedidos/cliente.html", {
            "accion": "0"
        })


def personal(request):
    today =  time.strftime('%Y-%m-%d')
    pedidos_contados = []
    for cliente in Cliente.objects.all():
        pedidos_cliente= Pedido.objects.filter(cliente=cliente)
        i= pedidos_cliente.count()
        pedidos_contados.append([cliente, i])
    pedidos_contados.sort(key=itemgetter(1), reverse=True)
    if request.method == 'POST':
        if request.POST['submit'] == "Asignar":
            if Reparto.objects.filter(nombre=request.POST['nombre'], identificador=request.POST['identificador']).count() == 0:
                nuevo_reparto = Reparto(nombre=request.POST['nombre'], identificador=request.POST['identificador'], dia=request.POST['dia'])
                nuevo_reparto.save()
                pedido_existente = Pedido.objects.get(id=request.POST['pedido_id'])
                pedido_existente.reparto = nuevo_reparto
                pedido_existente.estado = "en reparto"
                pedido_existente.save()
            else:
                reparto_existente = Reparto.objects.get(nombre=request.POST['nombre'], identificador=request.POST['identificador'])
                pedido_existente = Pedido.objects.get(id=request.POST['pedido_id'])
                pedido_existente.reparto = reparto_existente
                pedido_existente.estado = "en reparto"
                pedido_existente.save()

            return render(request, "pedidos/personal.html", {
                'pedidos_preparados' : Pedido.objects.filter(estado="preparado"),
                'repartos_hoy' : Reparto.objects.filter(dia=datetime.date.today()),
                'pedidos_no_asignados' : Pedido.objects.filter(estado="no asignado"),
                'articulos' : Articulo.objects.all(),
                'pedidos_contados' : pedidos_contados,
                'pedidos_enreparto' : Pedido.objects.filter(estado="en reparto"),
                'today': today
            })
        elif request.POST['submit'] == "preparado":
            pedido_actualizado = Pedido.objects.get(id=request.POST['pedido_id'])
            pedido_actualizado.estado = "preparado"
            pedido_actualizado.save()
            articulo_actualizado=Articulo.objects.get(id=pedido_actualizado.articulo.id)
            articulo_actualizado.stock_actual -= pedido_actualizado.cantidad
            articulo_actualizado.save()
            return render(request, "pedidos/personal.html", {
                'pedidos_preparados' : Pedido.objects.filter(estado="preparado"),
                'repartos_hoy' : Reparto.objects.filter(dia=datetime.date.today()),
                'pedidos_no_asignados' : Pedido.objects.filter(estado="no asignado"),
                'articulos' : Articulo.objects.all(),
                'pedidos_contados' : pedidos_contados,
                'pedidos_enreparto' : Pedido.objects.filter(estado="en reparto"),
                'today': today
            })
        elif request.POST['submit'] == "Guardar cambios":
            for art in Articulo.objects.all():
                art.nombre = request.POST['nombre_'+str(art.id)]
                art.precio = request.POST['precio_'+str(art.id)]
                art.stock_actual = request.POST['sa_'+str(art.id)]
                art.stock_maximo = request.POST['sm_'+str(art.id)]
                art.save()
            return render(request, "pedidos/personal.html", {
                'pedidos_preparados' : Pedido.objects.filter(estado="preparado"),
                'repartos_hoy' : Reparto.objects.filter(dia=datetime.date.today()),
                'pedidos_no_asignados' : Pedido.objects.filter(estado="no asignado"),
                'articulos' : Articulo.objects.all(),
                'pedidos_contados' : pedidos_contados,
                'pedidos_enreparto' : Pedido.objects.filter(estado="en reparto"),
                'today': today
            })
        elif request.POST['submit']=="Crear":
            nuevo_articulo = Articulo(
                nombre= request.POST['nombre_nuevo'],
                precio= request.POST['precio_nuevo'],
                stock_actual= request.POST['sa_nuevo'],
                stock_maximo= request.POST['sm_nuevo'],
            )
            nuevo_articulo.save()
            return render(request, "pedidos/personal.html", {
                'pedidos_preparados' : Pedido.objects.filter(estado="preparado"),
                'repartos_hoy' : Reparto.objects.filter(dia=datetime.date.today()),
                'pedidos_no_asignados' : Pedido.objects.filter(estado="no asignado"),
                'articulos' : Articulo.objects.all(),
                'pedidos_contados' : pedidos_contados,
                'pedidos_enreparto' : Pedido.objects.filter(estado="en reparto"),
                'today': today
            })

        elif request.POST['submit']=="Actualizar":
            pedido_nuevo_estado = Pedido.objects.get(id=request.POST['id_ped'])
            pedido_nuevo_estado.estado = request.POST['estado']
            pedido_nuevo_estado.save()

    return render(request, "pedidos/personal.html", {
        'pedidos_preparados' : Pedido.objects.filter(estado="preparado"),
        'repartos_hoy' : Reparto.objects.filter(dia=datetime.date.today()),
        'pedidos_no_asignados' : Pedido.objects.filter(estado="no asignado"),
        'articulos' : Articulo.objects.all(),
        'pedidos_contados' : pedidos_contados,
        'pedidos_enreparto' : Pedido.objects.filter(estado="en reparto"),
        'today': today
    })