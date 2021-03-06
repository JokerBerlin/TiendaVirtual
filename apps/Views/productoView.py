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
@permission_required('is_admin')
def listarProducto(request):
    oProductos = Producto.objects.all()
    precios=[]
    #for oProducto in oProductos:
    for oProducto in oProductos:
        nuevo={}
        try:
            oUltimoP=Producto_lote.objects.filter(producto_id=oProducto).latest('id')
            print(oUltimoP)
            nuevo['id'] = oProducto.id
            nuevo['cantidad'] = oUltimoP.cantidad
        except Exception as e:
            print(e)
            nuevo['id'] = oProducto.id
            nuevo['cantidad'] = 0
        precios.append(nuevo)
    #nuevo={}
    print(precios)

    template = loader.get_template('producto/listar.html')
    context = {'oProducto':oProductos,'precios':precios,}
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

@login_required
@permission_required('is_admin')
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

@login_required
@permission_required('is_admin')
def detalleProducto(request,producto_id):
    oProducto = Producto.objects.get(id=producto_id)
    template = loader.get_template('producto/detalle.html')
    context = {'oProducto':oProducto,}
    return HttpResponse(template.render(context, request))


@login_required
@permission_required('is_admin')
def detalleCompraAdmin(request, compra_id):
    oCompra = Compra.objects.get(id=compra_id)
    oProductoCompras = Producto_compra.objects.filter(compra_id = compra_id)
    oProducto = []
    for oProductoCompra in oProductoCompras:
        nuevo = {}
        nuevo['id'] = oProductoCompra.id
        montoSubTotal = oProductoCompra.cantidad * oProductoCompra.producto.precioOfertaProducto
        nuevo['subTotal'] = montoSubTotal
        oProducto.append(nuevo)
    oStIgv = round(oCompra.montoTotal / 1.18,1)
    oIgv = round(oCompra.montoTotal - oStIgv,1)

    oCategorias = Categoria.objects.all()
    template = loader.get_template('compra/detalle.html')
    context = {'oCategorias':oCategorias,'oCompra':oCompra,'oProductoCompras':oProductoCompras,'oProducto':oProducto,'oStIgv':oStIgv,'oIgv':oIgv,}
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('is_admin')
def reporteCantidadProducto(request):
    oProductos = Producto.objects.all()
    productos = []
    for oProducto in oProductos:
        nuevo = {}
        try:
            ProductoLote = Producto_lote.objects.filter(producto_id=oProducto.id).latest('id')

            nuevo['nombre'] = oProducto.nombreProducto
            nuevo['cantidad'] = ProductoLote.cantidad
        except Exception as e:
            nuevo['nombre'] = oProducto.nombreProducto
            nuevo['cantidad'] = 0
        productos.append(nuevo)

    template = loader.get_template('reporte/cantidadProductos.html')
    context = {'productos':productos,}
    return HttpResponse(template.render(context, request))


def reporteProductosMasVendidos(request):
    oProductos = Producto.objects.all()
    productos = []
    for oProducto in oProductos:
        nuevo = {}
        try:
            ProductoCompra = Producto_compra.objects.filter(producto_id=oProducto.id)
            cantidadVendido = 0
            for productoC in ProductoCompra:
                cantidadVendido = cantidadVendido + productoC.cantidad
            nuevo['nombre'] = oProducto.nombreProducto
            nuevo['cantidad'] = cantidadVendido
        except Exception as e:
            nuevo['nombre'] = oProducto.nombreProducto
            nuevo['cantidad'] = 0
        productos.append(nuevo)

    template = loader.get_template('reporte/cantidadProductos.html')
    context = {'productos':productos,}
    return HttpResponse(template.render(context, request))
