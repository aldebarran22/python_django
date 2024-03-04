from django.contrib import admin

# Register your models here.
from tutorial.models import Fotografia, Author, Book, Publisher


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "age")


class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)


class BookAdmin(admin.ModelAdmin):
    # Columnas del listado
    list_display = ("isbn", "name", "price")
    # Campos de búsqueda
    search_fields = ("name",)
    # Propiedad del book (FK), dentro de la FK la columna que nos interesa
    list_filter = ("publisher__name",)


# Registrar las clases del modelo para poder
# utilizarlas desde el panel de administración
admin.site.register(Fotografia)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
