from django.db import models

# Create your models here.


class Categoria(models.Model):
    # Los campos del categoria
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)


class Proveedor(models.Model):
    # Los campos del proveedor
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)


class Producto(models.Model):
    # Los campos del producto
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    existencias = models.IntegerField()
    existenciasmin = models.IntegerField()

    # Claves foráneas:
    # 1 categoria N productos
    # 1 prov. N productos
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)
    dni = models.CharField(max_length=15)
    fecha_alta = models.DateField(null=True) # Fecha vacía
    # 1 cliente -> N pedidos

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    cargo = models.CharField(max_length=40)
    fecha_alta = models.DateField(null=True) # Fecha vacía
    # 1 empleado -> N pedidos

class Empresa(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    # 1 empresa -> N pedidos