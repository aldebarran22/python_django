"""tutorial_biblio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import tutorial.views
from django.conf.urls.static import static
import tutorial_biblio.settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tutorial.views.index, name="inicio"),
    path("libros", tutorial.views.libros, name="libros"),
    path("galeria", tutorial.views.galeria, name="galeria"),
    path("info_request", tutorial.views.info_request, name="info_request"),
    path("formulario", tutorial.views.formulario, name="formulario"),    
]

if tutorial_biblio.settings.DEBUG:
    urlpatterns += static(
        tutorial_biblio.settings.MEDIA_URL,
        document_root=tutorial_biblio.settings.MEDIA_ROOT,
    )
