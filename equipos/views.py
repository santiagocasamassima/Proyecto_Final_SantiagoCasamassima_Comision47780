from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import *
from .models import equipos, proveedores, articulos
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    context = {
        "equipo" : "electrocardiografo"
    }
    http_response = render(
        request = request,
        template_name="index.html",
        context = context
    )
    return http_response

def lista_equipos(request):
    
    contexto = {
        "equipos": equipos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='equipos/lista_equipos.html',
        context=contexto,
    )
    return http_response

@login_required
def cargar_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            id = data["id"]
            nombre = data["nombre"]
            descripcion = data["descripcion"]
            ubicacion = data["ubicacion"]
        eq = equipos(nombre=nombre, descripcion=descripcion, ubicacion=ubicacion)
        eq.save()

        successful_url = reverse("lista_equipos")
        return redirect(successful_url)

    else:
        form = EquipoForm()
    http_response = render(
    request= request,
    template_name="equipos/carga_equipos.html",
    context={"form":form}
    )
    return http_response   
 
@login_required
def editar_equipo(request, id):
    equipo = equipos.objects.get(id=id)
    if request.method == "POST":
        form = EquipoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            equipo.id = data["id"]
            equipo.nombre = data["nombre"]
            equipo.descripcion = data["descripcion"]
            equipo.ubicacion = data["ubicacion"]
            
            equipo.save()

            successful_url = reverse("lista_equipos")
            return redirect(successful_url)
    else:
        #descargar formulario con data actual
        inicial = {
            "id": equipo.id,
            "nombre": equipo.nombre,
            "descripcion": equipo.descripcion,
            "ubicacion": equipo.ubicacion,
        }
        form = EquipoForm(initial=inicial)
    return render(
        request= request,
        template_name="equipos/carga_equipos.html",
        context={"form":form}
    )    

@login_required
def eliminar_equipo(request, id):
     equipo = equipos.objects.get(id=id) 
     
     if request.method == "POST":
        equipo.delete()
        
        url_exitosa = reverse("lista_equipos")
        return redirect(url_exitosa)
     
def busqueda_equipo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
    # Filtrado
        eq = equipos.objects.filter(
            Q(nombre__icontains=busqueda) | Q(ubicacion__contains=busqueda)
        )
        
        contexto = {
            "equipos": eq,
        }
        http_response = render(
            request=request,
            template_name="equipos/lista_equipos.html",
            context=contexto,
        )
        return http_response

def lista_proveedores(request):
    
    contexto = {
        "proveedores": proveedores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='equipos/lista_proveedores.html',
        context=contexto,
    )
    return http_response

@login_required
def cargar_proveedores(request):
    if request.method == "POST":
        form = ProveedoresForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            nombre = data["nombre"]
            contacto = data["contacto"]
            datos_adicionales = data["datos_adicionales"]
        pr = proveedores(nombre=nombre, contacto=contacto, datos_adicionales=datos_adicionales)
        pr.save()

        successful_url = reverse("lista_proveedores")
        return redirect(successful_url)

    else:
        form = ProveedoresForm()
    http_response = render(
    request= request,
    template_name="equipos/carga_proveedores.html",
    context={"form":form}
    )
    return http_response     

@login_required
def editar_proveedor(request, id):
    proveedor = proveedores.objects.get(id=id)
    if request.method == "POST":
        form = ProveedoresForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            proveedor.nombre = data["nombre"]
            proveedor.contacto = data["contacto"]
            proveedor.datos_adicionales = data["datos_adicionales"]            
            
            proveedor.save()

            successful_url = reverse("lista_proveedores")
            return redirect(successful_url)
    else:
        #descargar formulario con data actual
        inicial = {
            "nombre": proveedor.nombre,
            "contacto": proveedor.contacto,
            "datos_adicionales": proveedor.datos_adicionales,
        }
        form = ProveedoresForm(initial=inicial)
    return render(
        request= request,
        template_name="equipos/carga_proveedores.html",
        context={"form":form}
    )  
  
@login_required
def eliminar_proveedor(request, id):
     proveedor = proveedores.objects.get(id=id) 
     
     if request.method == "POST":
        proveedor.delete()
        
        url_exitosa = reverse("lista_proveedores")
        return redirect(url_exitosa) 

def busqueda_proveedor(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
    # Filtrado
        pro = proveedores.objects.filter(
            Q(nombre__icontains=busqueda) | Q(contacto__contains=busqueda)
        )
        
        contexto = {
            "proveedores": pro,
        }
        http_response = render(
            request=request,
            template_name="equipos/lista_proveedores.html",
            context=contexto,
        )
        return http_response    

@login_required
def cargar_articulo(request):
    if request.method == "POST":
        form = ArticulosForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data 
            id = data["id"]
            titulo = data["titulo"]
            fecha = data["fecha"]
            mensaje = data["mensaje"]
            ar = articulos(titulo=titulo, fecha=fecha, mensaje=mensaje, creador=request.user)
            ar.save()

            successful_url = reverse("lista_articulos")
            return redirect(successful_url)

    else:
        form = ArticulosForm()
    http_response = render(
    request= request,
    template_name="equipos/carga_articulos.html",
    context={"form":form}
    )
    return http_response    

def lista_articulos(request):    
    contexto = {
        "articulos": articulos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='equipos/lista_articulos.html',
        context=contexto,
    )
    return http_response

@login_required
def eliminar_articulo(request, id):
     articulo = articulos.objects.get(id=id) 
     
     if request.method == "POST":
        articulo.delete()
        
        url_exitosa = reverse("lista_articulos")
        return redirect(url_exitosa)

@login_required
def editar_articulo(request, id):
    articulo = articulos.objects.get(id=id)
    if request.method == "POST":
        form = ArticulosForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            articulo.id = data["id"]
            articulo.titulo = data["titulo"]
            articulo.fecha = data["fecha"]
            articulo.mensaje = data["mensaje"]
                 
            articulo.save()

            successful_url = reverse("lista_articulos")
            return redirect(successful_url)
    else:
        #descargar formulario con data actual
        inicial = {
            "id": articulo.id,
            "titulo": articulo.titulo,
            "fecha": articulo.fecha,
            "mensaje": articulo.mensaje,            
        }
        form = ArticulosForm(initial=inicial)
    return render(
        request= request,
        template_name="equipos/carga_articulos.html",
        context={"form":form}
    )   

def busqueda_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
    # Filtrado
        art = articulos.objects.filter(
            Q(titulo__icontains=busqueda) | Q(mensaje__contains=busqueda)
        )
        
        contexto = {
            "articulos": art,
        }
        http_response = render(
            request=request,
            template_name="equipos/lista_articulos.html",
            context=contexto,
        )
        return http_response 
    
class ArticuloDetailView(LoginRequiredMixin, DetailView):
    model = articulos
    success_url = reverse_lazy('lista_articulos')

def about(request):
    return render(request, 'equipos/acercaDeMi.html', {})