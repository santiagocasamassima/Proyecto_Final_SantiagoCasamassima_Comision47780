from django.urls import path

from equipos.views import lista_equipos, cargar_equipo, busqueda_equipo, lista_proveedores, cargar_proveedores, busqueda_proveedor, editar_proveedor, eliminar_proveedor, eliminar_equipo, editar_equipo, editar_articulo, busqueda_articulo, eliminar_articulo, lista_articulos, cargar_articulo





urlpatterns = [
    path("lista-equipos/", lista_equipos, name="lista_equipos"),
    path("carga-equipos/", cargar_equipo, name="cargar_equipo"),
    path("buscar-equipos/", busqueda_equipo, name="busqueda_equipo"),    
    path("elimina-equipos/<int:id>/" , eliminar_equipo, name="eliminar_equipo"),
    path("edita-equipos/<int:id>/" , editar_equipo, name="editar_equipo"),
    path("lista-proveedores/", lista_proveedores, name="lista_proveedores"),
    path("carga-proveedores/", cargar_proveedores, name="cargar_proveedores"),
    path("buscar-proveedores/", busqueda_proveedor, name="busqueda_proveedor"),    
    path("elimina-proveedores/<int:id>/" , eliminar_proveedor, name="eliminar_proveedor"),
    path("edita-proveedores/<int:id>/" , editar_proveedor, name="editar_proveedor"),
    path("lista-articulos/", lista_articulos, name="lista_articulos"),
    path("carga-articulos/", cargar_articulo, name="cargar_articulo"),
    path("buscar-articulos/", busqueda_articulo, name="busqueda_articulo"),
    path("elimina-articulos/<int:id>/" , eliminar_articulo, name="eliminar_articulo"),
    path("edita-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
     ]