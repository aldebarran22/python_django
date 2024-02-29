from django.contrib import admin

# Register your models here.
from tutorial.models import Fotografia

# Registrar las clases del modelo para poder
# utilizarlas desde el panel de administración
admin.site.register(Fotografia)
