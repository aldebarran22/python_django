from django.contrib import admin
from tutorial.models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

class BookAdmin(admin.ModelAdmin):
    # Campos a mostrar en el lista
    list_display = ('isbn','name','price','date','publisher')
    # Normalmente asociado a una foreignkey
    # propiedadbook__propiedadpublisher
    list_filter = ('publisher__name',)
    # Para buscar texto tecleando: 
    search_fields = ('name',)
    date_hierarchy = 'date'
    ordering = ('-date',)
    filter_horizontal=('authors',)

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','foto')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Store)
admin.site.register(Fotografia, FotografiaAdmin)
