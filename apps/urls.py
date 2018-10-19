from django.urls import path, re_path
from apps.views import *
from apps.Views.productoView import *
from django.conf import settings
from django.conf.urls.static import static
app_name='producto'
urlpatterns = [
    path('Producto/registrar/', registrarProducto, name = "crear_producto"),
    path('Producto/listar/', listarProducto, name = "listar_producto"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
