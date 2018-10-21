from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404


def pruebaTienda(request):
    template = loader.get_template('tienda/mostrarTienda.html')
    context = {}
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
