from django.urls import path, re_path
from apps.views import *
from apps.Views.productoView import *
app_name='producto'
urlpatterns = [
    path('producto/registrar/', registrarProducto, name = "crear_producto"),

]
