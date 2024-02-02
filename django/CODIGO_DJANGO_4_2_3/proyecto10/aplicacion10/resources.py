from import_export import resources
from .models import Persona

class PersonResource(resources.ModelResource):
    class Meta:
        model = Persona