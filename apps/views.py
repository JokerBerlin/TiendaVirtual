from django.shortcuts import render

# Create your views here.
def registrarProducto(request):
    template = 'producto/registrar.html'
    return render(request,template)
