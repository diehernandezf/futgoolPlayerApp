from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('registro', views.cargarRegistro),
    path('registrarForm', views.agregarUsuario),
    path('evaluarRendimiento', views.mostrarDatosUsuario),
    path('evaluar_rendimiento/<int:usuario_id>/', views.evaluar_rendimiento, name='evaluar_rendimiento'),
]