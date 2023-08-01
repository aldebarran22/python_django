# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clientes(models.Model):
    idcliente = models.TextField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Detallespedido(models.Model):
    idpedido = models.AutoField(primary_key=True)  # The composite primary key (idpedido, idproducto) found, that is not supported. The first column is selected.
    idproducto = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallespedido'


class Empleados(models.Model):
    nombre = models.TextField(blank=True, null=True)
    cargo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'


class Empresasenvios(models.Model):
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresasenvios'


class Pedidos(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idcliente = models.TextField(blank=True, null=True)
    idempleado = models.IntegerField(blank=True, null=True)
    idempresaenvio = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Productos(models.Model):
    nombre = models.TextField(blank=True, null=True)
    idcategoria = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    existencias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'
