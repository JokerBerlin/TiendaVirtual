from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from apps.models import *
from apps.formularios.productoForm import *
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

@login_required
@permission_required('is_admin')
def listarLote(request):
    oLote = Lote.objects.all()
    template = loader.get_template('almacen/listarLote.html')
    oProductos = []
    for lote in oLote:
        oLoteProducto = Producto_lote.objects.filter(lote_id=lote.id)
        for oloPro in oLoteProducto:
            oNuevo={}
            oNuevo['id']=lote.id
            oNuevo['producto']=oloPro.producto.nombreProducto
            oNuevo['cantidad']=oloPro.cantidad
            oNuevo['cantidadInicial']=oloPro.cantidadinicial
            oProductos.append(oNuevo)
    print(oProductos)
    context = {'oLote':oLote,'oProductos':oProductos,}
    return HttpResponse(template.render(context, request))



@csrf_exempt
def registrarLoteAjax(request):
    if request.method == 'POST':
            Datos = json.loads(request.body)
            print(Datos)
        #Dato = json.loads(request.body)
        #Dato = request.POST
            nombreProveedor = Datos['oProveedor']
            # if nombreProveedor.isdigit() == False :
            #     nombreProveedor = Proveedor.objects.get(nombre=nombreProveedor).documento

            oProveedor = Proveedor.objects.get(nombreProveedor=nombreProveedor)
            print(oProveedor.nombreProveedor)
            tipoRecibo= Datos['oRecibo']
            numeroRecibo = Datos['oNumRecibo']
            oLote= Lote(tipoComprobante=tipoRecibo, nroComprobante=numeroRecibo, proveedor_id=oProveedor.id)
            oLote.save()

            oProductoLotes= Datos['oProductoLote']
            for oProductoLote in oProductoLotes:
                print(oProductoLote)
                cantidad= float(oProductoLote[0])
                nombreProducto=oProductoLote[1]
                oProducto= Producto.objects.get(nombreProducto= nombreProducto)
                oAlmacenese = Producto_lote.objects.filter(producto_id=oProducto.id).exists()
                #print(oAlmacenese)
                if oAlmacenese == True:
                    oUltimoP=Producto_lote.objects.filter(producto_id=oProducto).latest('id')
                    cantidadIni = float(oUltimoP.cantidad)

                    cantidadNueva = cantidadIni + cantidad
                    oProducto_lot = Producto_lote(cantidad=cantidadNueva, cantidadinicial= cantidadIni, lote_id= oLote.id, producto_id= oProducto.id)
                    oProducto_lot.save()
                else:
                    #oUltimoP=Producto_almacens.objects.filter(producto_id=oProducto).latest('id')
                    oProducto_lot = Producto_lote(cantidad=cantidad, cantidadinicial= 0, lote_id= oLote.id, producto_id= oProducto.id)
                    oProducto_lot.save()


            return HttpResponse(json.dumps({'exito':1}), content_type="application/json")

        #datos_list = json.loads(datos[0])

        #return render(request, '/pedido/listar.html')
    else:
        context ={}
        return render(request, 'almacen/lote.html', context)

def eliminarLoteAjax(request):
    pk = request.POST.get('identificador_id')
    oLote = Lote.objects.get(id=pk)
    oLoteProductos = Producto_lote.objects.filter(lote_id=oLote.id)
    for oLoteProducto in oLoteProductos:
        oLoteP = Producto_lote.objects.get(id=oLoteProducto.id)
        oLoteP.delete()
    oLote.delete()
    response = {}
    return JsonResponse(response)
