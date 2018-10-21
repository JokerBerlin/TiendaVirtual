from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404


def pruebaTienda(request):
    template = loader.get_template('tienda\mostrarTienda.html')
    context = {}
    return HttpResponse(template.render(context, request))


def mostrarContacto(request):
    template = loader.get_template('tienda\contacto.html')
    context = {}
    return HttpResponse(template.render(context, request))
