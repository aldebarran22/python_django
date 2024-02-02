from django.contrib import admin

# Register your models here.
from aplicacion7.models import Empleado, Empresa,Categoria, Producto
from aplicacion7.models import Pedido, Cliente, Proveedor

class EmpresaAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion')
    search_fields = ('nombre', )

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion')

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio', 'existencias', 'categoria')

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor)
admin.site.register(Categoria, CategoriaAdmin)


