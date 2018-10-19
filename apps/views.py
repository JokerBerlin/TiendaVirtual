from django.shortcuts import render, render_to_response, redirect
from apps.models import *
from apps.formularios.productoForm import *
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def mostrarInicio(request):
    template = loader.get_template('login/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
