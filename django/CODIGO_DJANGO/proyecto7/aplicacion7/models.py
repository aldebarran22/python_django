from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    empresa = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    existencias = models.IntegerField()
    existencias_min = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.direccion

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    cargo = models.CharField(max_length=40)
    fecha_alta = models.DateField()

class Productos_Pedidos(models.Model):
    """Esta clase representa la relación entre el pedido y los productos"""
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


