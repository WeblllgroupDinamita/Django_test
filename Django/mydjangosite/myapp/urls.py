"""
URL configuration for mydjangosite project.

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
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', views.index, name='index'),
#CRUDS FOR APP
    path('', login_required(views.mostrar), name='login'),
    path('datos', login_required(views.mostrar), name='mostrar'),
    path('datos/agregar', login_required(views.agregar_dato), name='agregar_dato'),
    path('datos/modificar/<int:id>', login_required(views.modificar_dato), name='modificar_dato'),
    path('datos/eliminar/<int:id>', login_required(views.eliminar_dato), name='eliminar_dato'),

]
