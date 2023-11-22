from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from perfiles.forms import UserRegisterForm



def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse("inicio")
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request = request,
        template_name="perfiles/registro.html",
        context={"form": formulario},
    )
