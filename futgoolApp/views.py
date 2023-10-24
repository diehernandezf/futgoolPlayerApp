from django.shortcuts import render, redirect
from .models import *

import os
from django.conf import settings
# Create your views here.

def cargarInicio(request):
    return render(request, "inicio.html")

def cargarRegistro(request):
    usuarios = Usuario.objects.all()
    return render(request, "registro.html",{"users":usuarios})

def agregarUsuario(request):
    v_nombre = request.POST['txtNombre']
    v_email = request.POST['txtEmail']
    v_contrasena = request.POST['txtContrasena']

    Usuario.objects.create(nombre = v_nombre, email = v_email, password = v_contrasena)

    return redirect('/registro')