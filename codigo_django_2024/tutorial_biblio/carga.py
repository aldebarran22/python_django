from tutorial.models import Author, Publisher, Book, Store
from tutorial import settings
from random import randint

import sys
import django
import os

sys.path.append("./tutorial")

settings.configure()
os.environ["DJANGO_SETTINGS_MODULE"] = "tutorial.settings"

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()


# Generar datos:
for i in range(1, 21):
    autor = Author(name="Autor " + str((i + 1)), age=randint(20, 60))
    autor.save()
