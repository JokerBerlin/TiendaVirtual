
##paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    try:
        oProductoLote = Producto_lote.objects.filter(producto_id=oProducto.id).latest('id')
    except Exception as e:
        oProducto = ''
        oProductoLote = ''

    # userid = request.user.id
    # id_usuario = User.objects.get(id=userid)
    template = loader.get_template('tienda/detalleProducto.html')
    oCategorias = Categoria.objects.all()
    context = {'oProducto':oProducto,'oCategorias':oCategorias,'oProductoLote':oProductoLote,}
    return HttpResponse(template.render(context, request))


def listarCompra(request):
    try:
        userid = request.user.id
        id_usuario = User.objects.get(id=userid)
        oCompras = Compra.objects.filter(user_id=id_usuario.id).order_by('-id')
        template = loader.get_template('tienda/mostrarCompra.html')
        oCategorias = Categoria.objects.all()
        context = {'oCategorias':oCategorias,'oCompras':oCompras,}
        return HttpResponse(template.render(context, request))
    except Exception as e:
        oCompra = Compra.objects.all().latest('id')
        compra_id = str(oCompra.id)
        return redirect('/Tienda/detalleCompra/'+compra_id+'/')

def detalleCompra(request, compra_id):
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
    template = loader.get_template('tienda/detalleCompra.html')
    context = {'oCategorias':oCategorias,'oCompra':oCompra,'oProductoCompras':oProductoCompras,'oProducto':oProducto,'oStIgv':oStIgv,'oIgv':oIgv,}
    return HttpResponse(template.render(context, request))

def listarCarrito(request):
    try:
        userid = request.user.id
        id_usuario = User.objects.get(id=userid)
        oCarroCompra = carroCompra.objects.filter(estado = True, user_id=id_usuario.id)
    except Exception as e:
        oCarroCompra = carroCompra.objects.filter(estado=True,user_id=None)
    print(oCarroCompra)
    cantidadPro = []
    for carro in oCarroCompra:
        oLote = Producto_lote.objects.filter(producto_id=carro.producto_id).latest('id')
        nuevo = {}
        nuevo["id"] = carro.id
        nuevo["cantidad"] = oLote.cantidad
        cantidadPro.append(nuevo)
    template = loader.get_template('tienda/listarCarrito.html')
    oCategorias = Categoria.objects.all()
    context = {'oCategorias':oCategorias,'oCarroCompra':oCarroCompra,'cantidadPro':cantidadPro,}
    return HttpResponse(template.render(context, request))

def mostrarPago(request):
    if request.method == 'POST':
        Datos = request.POST
        try:
            oMedioPago = Medio_pago.objects.get(nombreEnTarjeta=Datos["name"],numeroTarjeta=Datos["number"],ccv=Datos["security-code"],fechaExpiracion=Datos["expiration-month-and-year"])
            print('Exito')
            print(oMedioPago.nombreEnTarjeta)
            return redirect('/Tienda/comprar/')
        except Exception as e:
            error = 'Los datos ingresados son incorrectos'
            template = loader.get_template('tienda/pago.html')
            oCategorias = Categoria.objects.all()
            context = {'oCategorias':oCategorias, 'error':error,}
            return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('tienda/pago.html')
        oCategorias = Categoria.objects.all()
        context = {'oCategorias':oCategorias}
        return HttpResponse(template.render(context, request))

def realizarPago(request):
    try:
        userid = request.user.id
        id_usuario = User.objects.get(id=userid)
        oCarroCompra = carroCompra.objects.filter(estado = True, user_id=id_usuario.id)
    except Exception as e:
        oCarroCompra = carroCompra.objects.filter(estado=True,user_id=None)
    cantidadPro = []
    montoTotal = 0
    for carro in oCarroCompra:
        oProducto = Producto.objects.get(id=carro.producto_id)
        subTotal = float(oProducto.precioOfertaProducto) * int(carro.cantidad)
        montoTotal = montoTotal + subTotal
    if request.method == 'POST':
        try:
            userid = request.user.id
            id_usuario = User.objects.get(id=userid)
            oCompra = Compra()
            oCompra.tipoComprobante = "Boleta"
            oCompra.nroComprobante = "001-0000001"
            oCompra.montoTotal = montoTotal
            oCompra.user_id = id_usuario.id
            oCompra.save()
        except Exception as e:
            oCompra = Compra()
            oCompra.tipoComprobante = "Boleta"
            oCompra.nroComprobante = "001-0000001"
            oCompra.montoTotal = montoTotal
            oCompra.save()

        for carro in oCarroCompra:
            oCarro = carroCompra.objects.get(id=carro.id)
            oProductoCompra = Producto_compra()
            oProductoCompra.cantidad = oCarro.cantidad
            oProductoCompra.compra_id = oCompra.id
            oProductoCompra.producto_id = oCarro.producto_id
            oProductoCompra.save()
            oProductoLote = Producto_lote.objects.filter(producto_id=oCarro.producto_id).latest('id')
            oProductoLote.cantidadinicial = oProductoLote.cantidad
            cantidadNueva = oProductoLote.cantidad - oCarro.cantidad
            oProductoLote.cantidad = cantidadNueva
            oProductoLote.save()
            oCarro.delete()
        print('exito')
        return redirect('/Tienda/listarCompra/')
    else:
        template = loader.get_template('tienda/realizarCompra.html')
        oCategorias = Categoria.objects.all()
        context = {'oCategorias':oCategorias,'oCarroCompra':oCarroCompra,'cantidadPro':cantidadPro,}
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

def CategoriaProductoTienda(request, id):
    oCategorias = Categoria.objects.all()
    oProductos = Producto.objects.filter(categoria_id=id).order_by('-id')

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

def eliminarCarro(request, carro_id):
    oCarro = carroCompra.objects.get(id=carro_id)
    oCarro.delete()
    return redirect('/Tienda/carrito/listar/')

@csrf_exempt
def editarCarro(request):
    if request.method == 'POST':
            Datos = json.loads(request.body)
            idCarro = Datos['idCarro']
            cantidadN = Datos['cantidad']
            # if nombreProveedor.isdigit() == False :
            #     nombreProveedor = Proveedor.objects.get(nombre=nombreProveedor).documento

            oCarroCompra = carroCompra.objects.get(id=idCarro)
            oCarroCompra.cantidad = cantidadN
            oCarroCompra.save()

            return HttpResponse(json.dumps({'exito':1}), content_type="application/json")



@csrf_exempt
def CrearCarroAjax(request):
    if request.method == 'POST':
            Datos = json.loads(request.body)
            idProducto = Datos['idProducto']
            cantidad = Datos['cantidad']
            # if nombreProveedor.isdigit() == False :
            #     nombreProveedor = Proveedor.objects.get(nombre=nombreProveedor).documento

            oCarroCompra = carroCompra()
            oCarroCompra.cantidad = cantidad
            oCarroCompra.producto_id = idProducto
            try:
                userid = request.user.id
                id_usuario = User.objects.get(id=userid)
                oCarroCompra.user_id = id_usuario.id
            except Exception as e:
                print('none')
            oCarroCompra.save()

            return HttpResponse(json.dumps({'exito':1}), content_type="application/json")
