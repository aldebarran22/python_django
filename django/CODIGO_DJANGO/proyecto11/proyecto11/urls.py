"""
URL configuration for proyecto11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from aplicacion11.views import ListaLibros, DetalleLibro, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaLibros.as_view(), name='listalibros'),
    path('libros/', ListaLibros.as_view(), name='listalibros' ),
    path('libro/<int:pk>/', DetalleLibro.as_view(), name='verlibro'),
    path('nuevolibro/', BookCreate.as_view(), name='nuevolibro'),
    path('editalibro/<int:pk>/', BookUpdate.as_view(), name='editalibro'),
    path('borralibro/<int:pk>/', BookDelete.as_view(), name='borralibro')
]
