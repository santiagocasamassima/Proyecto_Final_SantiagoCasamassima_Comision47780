from django import forms

class EquipoForm(forms.Form):
    id = forms.CharField(required=True, max_length=400)
    nombre = forms.CharField(required=True, max_length=64)
    descripcion = forms.CharField(required=True, max_length=50000) 
    ubicacion = forms.CharField(required=True, max_length=256)

class ProveedoresForm(forms.Form):
    nombre = forms.CharField(max_length=128)
    contacto = forms.CharField(max_length=256)
    datos_adicionales = forms.CharField(max_length=256)

class ReferentesForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=128)
    interno = forms.CharField(required=True, max_length=30)