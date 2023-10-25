from django.shortcuts import render, redirect
from .models import Usuario, Calificacion

def cargarInicio(request):
    return render(request, "inicio.html")

def cargarRegistro(request):
    usuarios = Usuario.objects.all()
    return render(request, "registro.html", {"users": usuarios})

def agregarUsuario(request):
    v_nombre = request.POST['txtNombre']
    v_email = request.POST['txtEmail']
    v_contrasena = request.POST['txtContrasena']

    usuario = Usuario.objects.create(nombre=v_nombre, email=v_email, password=v_contrasena)

    return redirect('/registro', {"usuario": usuario})

def mostrarDatosUsuario(request):
    usuarios = Usuario.objects.all()
    return render(request, "evaluarRendimiento.html", {"usuarios": usuarios})

def evaluar_rendimiento(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)

    if request.method == "POST":
        calificacion_valor = int(request.POST['calificacion'])
        calificacion = Calificacion.objects.create(valor=calificacion_valor)
        usuario.calificaciones.add(calificacion)

    promedio = usuario.calcular_promedio()

    return render(request, 'evaluar_rendimiento.html', {'usuario': usuario, 'promedio': promedio})
