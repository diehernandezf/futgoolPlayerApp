from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('registro', views.cargarRegistro),
    path('registrarForm', views.agregarUsuario),
    #path('agregarProducto', views.cargarAgregarProducto),
    #path('agregarProductoForm',views.agregarProducto),
    #path('editarProducto/<sku>',views.cargarEditarProducto),
    #path('editarProducto',views.editarProducto),
    #path('eliminarProducto/<codigo_producto>',views.eliminarProducto),
    #path('login', views.cargarLogin),
    #path('registro', views.cargarRegistro),
    #path('usuarios', views.cargarAdministracionDeUsuarios)
]