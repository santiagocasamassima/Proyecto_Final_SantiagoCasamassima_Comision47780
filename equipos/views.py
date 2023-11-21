from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import equipos, proveedores, referentes
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q


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

def eliminar_equipo(request, id):
     equipo = equipos.objects.get(id=id)
     
     if request.method == "POST":
        equipo.delete()
        
        url_exitosa = reverse("lista_equipos")
        return redirect(url_exitosa)

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

def lista_referentes(request):
    
    contexto = {
        "referentes": referentes.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='equipos/lista_referentes.html',
        context=contexto,
    )
    return http_response

def cargar_referente(request):
    if request.method == "POST":
        form = ReferentesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            nombre = data["nombre"]
            interno = data["interno"]
        
        ref = referentes(nombre=nombre, interno=interno)
        ref.save()

        successful_url = reverse("lista_referentes")
        return redirect(successful_url)

    else:
        form = ReferentesForm()
    http_response = render(
    request= request,
    template_name="equipos/carga_referentes.html",
    context={"form":form}
    )
    return http_response

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
      