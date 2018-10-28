from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404

from apps.models import *

##paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    #Paginación
    paginator = Paginator(oProductos,9)

    page = request.GET.get('page')
    try:
        productoPagina = paginator.page(page)
    except PageNotAnInteger:
        productoPagina = paginator.page(1)
    except EmptyPage:
        productoPagina = paginator.page(paginator.num_pages)

    index = productoPagina.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    template = loader.get_template('tienda/listarProductos.html')
    context = {'oProductos':productoPagina,'oCategorias':oCategorias,'page_range': page_range}

    return HttpResponse(template.render(context, request))
