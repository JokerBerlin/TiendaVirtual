from django.urls import path, re_path
from apps.views import *
from apps.Views.productoView import *
from apps.Views.tiendaView import *
from apps.Views.usuarioView import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
app_name='producto'

urlpatterns = [
    path('', pruebaTienda),
    path('login/', Login),
    path('logout/', Logout),
    path('home/', mostrarInicio),
    path('Producto/registrar/', registrarProducto, name = "crear_producto"),
    path('Producto/listar/', listarProducto, name = "listar_producto"),
    path('Tienda/inicio/', pruebaTienda,name="mostrar_inicio"),
    path('Tienda/contacto/', mostrarContacto),
    path('Tienda/nosotros/', mostrarSobreNosotros),
    path('Tienda/terminos/', mostrarTerminos),
    path('Tienda/privacidad/', mostrarPrivacidad),
    path('Tienda/ayuda/', mostrarAyuda),
    path('Tienda/productoDetalle/<int:id>/', detalleProductoTienda),
    path('Tienda/carrito/listar/', listarCarrito),
    path('Tienda/pago/', mostrarPago),
    path('Tienda/Producto/listar/', listarProductoTienda),
    path('Tienda/CategoriaProducto/<int:id>/', CategoriaProductoTienda),
    #usuario
    path('Usuario/registrar/',RegistrarUsuario.as_view(), name="registrar_usuario"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
