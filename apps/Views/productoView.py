from django.shortcuts import render, render_to_response, redirect
from apps.models import *
from apps.formularios.productoForm import *
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse

def registrarProducto(request):
    if request.method == 'POST':
        #Datos = request.POST
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():

            producto = form.save()
            producto.save()
            return HttpResponseRedirect('crear_producto')
    else:
        form = ProductoForm()
            #return render(request, 'producto/registrar.html')
    template = loader.get_template('producto/registrar.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
