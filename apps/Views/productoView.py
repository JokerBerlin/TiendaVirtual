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

from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def buscarProductoAjax(request):
    if request.method == 'POST':
        Datos = json.loads(request.body)
        print(Datos)
        usuario=True
        if usuario==True:
            nombreProducto = Datos["nombreProducto"]
            jsonfinal = {}
            jsonfinal["productos"] = []
            try:
                oProductos = Producto.objects.filter(nombreProducto__icontains=nombreProducto)
                print(oProductos)
                for oProducto in oProductos:
                    jsonProducto = {}
                    jsonProducto["id"] = oProducto.id
                    jsonProducto["nombreProducto"] = oProducto.nombreProducto
                jsonfinal["productos"].append(jsonProducto)
                print("JSONFINAL", jsonfinal)
                return HttpResponse(json.dumps(jsonfinal), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'exito':0}), content_type="application/json")

def editarProducto(request,producto_id):
    oProducto = Producto.objects.get(id = producto_id)
    if request.method == 'POST':
        Datos = request.POST
        form = ProductoForm(request.POST or None, request.FILES, instance=oProducto)
        if form.is_valid():
            edit_prod=form.save(commit=False)
            form.save_m2m()
            edit_prod.status=True
            edit_prod.save()
            return redirect('/Producto/listar/')

        else:
            return render(request, '/Producto/error.html')
    else:
        form = ProductoForm(request.POST or None, instance=oProducto)
        return render(request, 'Producto/editar.html', {'form': form, 'oProducto':oProducto})
