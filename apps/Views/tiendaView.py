from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404

from apps.models import *

def pruebaTienda(request):
    oCategorias = Categoria.objects.all()
    oProductos = Producto.objects.all().order_by('-id')[:3]
    oProductosE = Producto.objects.all()
    template = loader.get_template('tienda/mostrarTienda.html')
    context = {'oCategorias':oCategorias,'oProductos':oProductos, 'oProductosE':oProductosE}
    return HttpResponse(template.render(context, request))


def mostrarContacto(request):
    template = loader.get_template('tienda/contacto.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def mostrarSobreNosotros(request):
    template = loader.get_template('tienda/sobreNosotros.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def mostrarTerminos(request):
    template = loader.get_template('tienda/terminos.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def mostrarPrivacidad(request):
    template = loader.get_template('tienda/privacidad.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def mostrarAyuda(request):
    template = loader.get_template('tienda/ayuda.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def detalleProductoTienda(request, id):
    oProducto = Producto.objects.get(id=id)
    template = loader.get_template('tienda/detalleProducto.html')
    oCategorias = Categoria.objects.all()
    context = {'oProducto':oProducto,'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def listarCarrito(request):
    template = loader.get_template('tienda/listarCarrito.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def mostrarPago(request):
    template = loader.get_template('tienda/pago.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias}
    return HttpResponse(template.render(context, request))

def listarProductoTienda(request):
    oCategorias = Categoria.objects.all()
    oProductos = Producto.objects.all().order_by('-id')
    print(oProductos)
    producto=[]
    for value in oProductos:
        print(value.id)
        if int(value.id) % 3 == 0:
            producto.append(value.id)
    print(producto)
    template = loader.get_template('tienda/listarProductos.html')
    context = {'oProductos':oProductos,'oCategorias':oCategorias,'producto':producto}
    return HttpResponse(template.render(context, request))
