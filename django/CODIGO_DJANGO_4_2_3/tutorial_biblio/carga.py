from tutorial.models import Author, Publisher, Book, Store
from random import randint

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()


# Generar datos:
for i in range(1,21):
    autor = Author(name='Autor ' + str((i+1)), age=randint(20,60))
    autor.save()

