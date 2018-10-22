from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404

from apps.models import *

def pruebaTienda(request):
    oCategorias = Categoria.objects.all()
    oProductos = Producto.objects.filter(categoria=2)[:3]
    template = loader.get_template('tienda/mostrarTienda.html')
    context = {'oCategorias':oCategorias,'oProductos':oProductos}
    return HttpResponse(template.render(context, request))


def mostrarContacto(request):
    template = loader.get_template('tienda/contacto.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mostrarSobreNosotros(request):
    template = loader.get_template('tienda/sobreNosotros.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mostrarTerminos(request):
    template = loader.get_template('tienda/terminos.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mostrarPrivacidad(request):
    template = loader.get_template('tienda/privacidad.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mostrarAyuda(request):
    template = loader.get_template('tienda/ayuda.html')
    context = {}
    return HttpResponse(template.render(context, request))

def detalleProductoTienda(request, id):
    oProducto = Producto.objects.get(id=id)
    template = loader.get_template('tienda/detalleProducto.html')
    context = {'oProducto':oProducto}
    return HttpResponse(template.render(context, request))

def listarCarrito(request):
    template = loader.get_template('tienda/listarCarrito.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mostrarPago(request):
    template = loader.get_template('tienda/pago.html')
    context = {}
    return HttpResponse(template.render(context, request))
