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

@csrf_exempt
def buscarProveedorAjax(request):
    if request.method == 'POST':
        Datos = json.loads(request.body)
        print(Datos)
        usuario=True
        if usuario==True:
            nombreProveedor = Datos["nombreProveedor"]
            print(nombreProveedor)
            jsonfinal = {}
            jsonfinal["proveedores"] = []
            try:
                oProveedores = Proveedor.objects.filter(nombreProveedor__icontains=nombreProveedor)
                print(oProveedores)
                for oProveedor in oProveedores:

                    jsonProveedor = {}
                    jsonProveedor["id"] = oProveedor.id
                    print(jsonProveedor["id"])
                    jsonProveedor["nombreProveedor"] = oProveedor.nombreProveedor
                    print(jsonProveedor)
                jsonfinal["proveedores"].append(jsonProveedor)
                print(jsonfinal)
                return HttpResponse(json.dumps(jsonfinal), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'exito':0}), content_type="application/json")
