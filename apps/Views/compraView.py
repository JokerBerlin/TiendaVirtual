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
def listarCompraUsuario(request):
    oCompra = Compra.objects.all().order_by('-id')
    template = loader.get_template('compra/listar.html')
    oProductos = []
    # for compra in oCompra:
    #     oLoteProducto = Producto_c.objects.filter(lote_id=lote.id).order_by('-id')
    #     for oloPro in oLoteProducto:
    #         oNuevo={}
    #         oNuevo['id']=lote.id
    #         oNuevo['producto']=oloPro.producto.nombreProducto
    #         oNuevo['cantidad']=oloPro.cantidad
    #         oNuevo['cantidadInicial']=oloPro.cantidadinicial
    #         oProductos.append(oNuevo)
    # print(oProductos)
    context = {'oCompra':oCompra,}
    return HttpResponse(template.render(context, request))
