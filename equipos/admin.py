from django.contrib import admin

# Register your models here.

from equipos.models import *

admin.site.register(equipos)

admin.site.register(proveedores)

admin.site.register(articulos)

