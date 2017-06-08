from django import forms

from apps.adopcion.models import Persona, Solicitud


class PersonaForm(forms.ModelForm):

    fields = [
        'nombre',
        'apellidos',
        'edad',
        'telefono',
        'email',
        'domicilio'
    ]

    labels = {
        'nombre': 'Nombre',
        'apellidos': 'Apellidos',
        'edad': 'Edad',
        'telefono': 'Telefono',
        'email': 'Email',
        'domicilio': 'Domicilio',
    }
    widgest = {
        'nombre':forms.TextInput(attrs={'class':'form-control'}),
        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
        'edad': forms.TextInput(attrs={'class': 'form-control'}),
        'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
    }


class SolicitudForm(forms.ModelForm):
    model = Solicitud
    fields = [
        'numeros_mascotas',
        'razones',
    ]
    labels = {
        'numeros_mascotas': 'Numeros_mascotas',
        'razones': 'Razones',
    }
    widgest = {
        'numeros_mascotas':forms.TextInput(attrs={'class':'form-control'}),
        'razones':forms.TextInput(attrs={'class':'form-control'}),

    }
