from django.urls import path

from equipos.views import lista_equipos, cargar_equipo, busqueda_equipo, lista_proveedores, cargar_proveedores, lista_referentes, cargar_referente, eliminar_equipo





urlpatterns = [
    path("lista-equipos/", lista_equipos, name="lista_equipos"),
    path("carga-equipos/", cargar_equipo, name="cargar_equipo"),
    path("buscar-equipos/", busqueda_equipo, name="busqueda_equipo"),
    path("lista-proveedores/", lista_proveedores, name="lista_proveedores"),
    path("carga-proveedores/", cargar_proveedores, name="cargar_proveedores"),
    path("lista-referentes/", lista_referentes, name="lista_referentes"),
    path("carga-referentes/", cargar_referente, name="cargar_referentes"),
    path("elimina-equipos/<int:id>/" , eliminar_equipo, name="eliminar_equipo"),

     ]