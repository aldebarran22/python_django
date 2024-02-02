"""
URL configuration for proyecto12 project.

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
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from django.contrib.auth.decorators import login_required, permission_required


import aplicacion12.views

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),    
    re_path('^accounts/login/$', LoginView.as_view(), name='login'),    
    re_path('^accounts/logout/$', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    re_path('^accounts/profile/$', aplicacion12.views.getInfoUser, name='profile'),
    path('', aplicacion12.views.getInfoUser, name='getinfo'),
    path('operacion1/', aplicacion12.views.operacion1, name='operacion1'),
    path('operacion2/', aplicacion12.views.operacion2, name='operacion2'),
    path('pagina1/', login_required(TemplateView.as_view(template_name='aplicacion12/pagina1.html')), name='pagina1'),
    path('escuchar_cancion/', permission_required('model_user.escuchar_cancion')(TemplateView.as_view(template_name='aplicacion12/escuchar_cancion.html')), name='escuchar_cancion'),
    path('bajar_cancion/', permission_required('model_user.bajar_cancion')(TemplateView.as_view(template_name='aplicacion12/bajar_cancion.html')), name='bajar_cancion'),
]

# Con esta NO para en la página de logout
#re_path('^accounts/logout/$', LogoutView.as_view(template_name='registration/logout.html',next_page='/accounts/profile'), name='logout'),