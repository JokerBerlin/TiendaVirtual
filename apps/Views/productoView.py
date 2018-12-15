from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from apps.models import *
from apps.formularios.productoForm import *
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings


@login_required
@permission_required('is_admin')
def registrarProducto(request):
    #if user.is_admin:
    if request.method == 'POST':
        #Datos = request.POST
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():

            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/Producto/listar/')
    else:
        form = ProductoForm()
            #return render(request, 'producto/registrar.html')
    template = loader.get_template('producto/registrar.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

@login_required
def listarProducto(request):
    oProducto = Producto.objects.all()
    print(oProducto)
    template = loader.get_template('producto/listar.html')
    context = {'oProducto':oProducto,}
    return HttpResponse(template.render(context, request))
