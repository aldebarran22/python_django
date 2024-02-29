import sys
import django
import os

sys.path.append("./tutorial")
from tutorial import settings

settings.configure()
os.environ["DJANGO_SETTINGS_MODULE"] = "tutorial.settings"

# SET DJANGO_SETTINGS_MODULE=tutorial.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from tutorial.models import Author, Publisher, Book, Store
n = Author.objects.count()
print("Numero de autores:", n)
