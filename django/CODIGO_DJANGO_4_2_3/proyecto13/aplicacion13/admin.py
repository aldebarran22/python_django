from django.contrib import admin
from aplicacion13.models import Lugar, VideoBook, Fotografia
# Register your models here.


class LugarAdmin(admin.ModelAdmin):
    list_display = ('lugar',)

class VideoBookAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha','descripcion')

class FotografiaAdmin(admin.ModelAdmin):
    list_display =  ('titulo','foto')

admin.site.register(Lugar, LugarAdmin)
admin.site.register(VideoBook, VideoBookAdmin)
admin.site.register(Fotografia, FotografiaAdmin)    
