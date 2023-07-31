from django.db import models

# Create your models here.

"""
Los productos (nombre, precio, existencias, existencias mínimas), se surten con
proveedores (nombre, empresa) que tienen que quedar registrados en el sistema. El
funcionamiento de la tienda es el siguiente: Un cliente (DNI, nombre, dirección, país,
fecha de alta, teléfono, email) llama por teléfono a la empresa y le recibe un Empleado
(nombre, cargo, fecha de alta) que genera un pedido con todos los productos que pide.
El pedido posteriormente se gestiona a través de una empresa de transportes
(nombre). Pensar en las relaciones de las entidades, que campos serían necesarios y
las relaciones: 1 a muchos y muchos a muchos. Del pedido tener en cuenta que
registra el cliente, el empleado, la compañía de transporte, fechas: recepción, pedido,
envío, lista de productos con su precio, cantidad y descuento, mantener también un
campo de observaciones. Registrar la app en settings.py
"""
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    description = models.TextField(max_length=30)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    existencias = models.IntegerField()
    existenciasmin = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=None)

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)
    dni = models.CharField(max_length=20)
    fecha_alta = models.DateField(null=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    cargo = models.CharField(max_length=40)
    fecha_alta = models.DateField()

class Empresa(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)

class Productos_Pedidos(models.Model):
    pedido = models.ForeignKey("Pedido", on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    descuento = models.FloatField()

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    fecha_pedido = models.DateField()
    fecha_envio = models.DateField(blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    productos = models.ManyToManyField(Producto, through=Productos_Pedidos)
