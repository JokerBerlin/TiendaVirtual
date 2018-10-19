from django.shortcuts import render, render_to_response, redirect
from apps.models import *
from apps.formularios.productoForm import *
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print (user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "login/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def mostrarInicio(request):
    template = loader.get_template('login/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
