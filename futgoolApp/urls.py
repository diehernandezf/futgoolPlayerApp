from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('crear_partido', views.crear_partido, name='crear_partido'),
    #path('agregarProducto', views.cargarAgregarProducto),
    #path('agregarProductoForm',views.agregarProducto),
    #path('editarProducto/<sku>',views.cargarEditarProducto),
    #path('editarProducto',views.editarProducto),
    #path('eliminarProducto/<codigo_producto>',views.eliminarProducto),
    #path('login', views.cargarLogin),
    #path('registro', views.cargarRegistro),
    #path('usuarios', views.cargarAdministracionDeUsuarios)
]