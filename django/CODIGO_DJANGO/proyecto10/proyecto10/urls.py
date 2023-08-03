"""
URL configuration for proyecto10 project.

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

import aplicacion10.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generar/', aplicacion10.views.generar),
    path('ver/', aplicacion10.views.ver),
    path('exportar/pdf/', aplicacion10.views.exportarpdf),
    path('exportar/csv/', aplicacion10.views.exportarcsv),
    path('exportar/csv2/', aplicacion10.views.exportarcsv2),
    path('exportar/excel/', aplicacion10.views.exportarexcel),
    path('exportar/json/', aplicacion10.views.exportarjson),
    path('exportar/xml/', aplicacion10.views.exportarxml),
]
