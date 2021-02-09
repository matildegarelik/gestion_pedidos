# Gestión de pedidos
Proyecto encargado por Ion A. @Zalowski a través de la plataforma http://freelancer.com
## Instrucciones
Para lanzar la aplicación a un servidor local, clonar el repositorio en tu ordenador. Luego, ingresar mediante la línea de comandos o CMD a la subcarpeta gestion_ventas y escribir la siguiente línea "python manage.py runserver". Esto lanzará el proyecto al local host, desde donde se podrá acceder.
## Detalles
El proyecto de deidca a la venta de artículos online. Para el reparto de las compras, es necesario asignar a un repartidor los productos para que puedan llegar al comprador al día siguiente. El objetivo es desarrollar una base de datos para la gestión de los repartos de ✭✭última milla✮✮.
El flujo de la información empieza en un pedido hasta que llega al cliente. En primer lugar, el usuario realiza una compra online de un número indeterminado de artículos. Todos los días a primera hora se hace un repaso de los pedidos del día anterior, mientras en el almacén se agrupan todos los artículos solicitados en pedidos para que sean enviados por un repartidor. El responsable de la gestión del reparto de pedidos se encarga de la asignación de un pedido, ya preparado, a un repartidor. El repartidor puede llevar más de un pedido en el camión y, por tanto, puede tener asignados en un solo reparto varios pedidos. Se pide desarrollar una base de datos en la que se pueda almacenar los artículos, clientes y pedidos y repartos. Los datos que se almacenarán de clientes son: nombre, apellido, dirección (calle y código postal), correo electrónico y edad. Cada artículo debe tener un nombre, el stock máximo, stock actual, precio. El pedido está formado por la relación de cliente, artículo y reparto, pero debe tener un atributo estado del pedido. Cada reparto tendrá asociado un nombre (ej. camión de Juan) y un identificador.
Además de esta definición, los datos deben cumplir el siguiente dominio. El código postal es un número de 5 cifras. El estado representa el cómo está el pedido en un momento dado y podrá ser: no asignado, en reparto, incidencia o repartido.
Se pide realizar los siguientes objetivos específicos que serán desarrollados en la memoria:
1. Crear un diagrama entidad relación ajustado a la descripción del problema.
2. Modelo lógico de la base de datos según el esquema conceptual.
3. Esquema físico de la base de datos implementado en SQLite.
4. Inserción de registros en la base de datos. Debe de haber al menos 3 registros de pedidos con cada uno de los diferentes estados.
5. El sistema de información permitirá el acceso a los datos con simples consultas. Por lo que se pide que Consulta a la base de datos de:
  a) Listado de clientes según el número de pedidos (acumulación) que ha realizado.
  b) Listado de los pedidos cuyo estado esté ✭✭en reparto✮✮.
 
## Tecnologías usadas
Desarrollo de aplicación web en Django, con una base de datos SQLite. 
