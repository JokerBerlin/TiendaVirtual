from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404, render_to_response, redirect

###
from django.contrib.auth import login, authenticate


from apps.models import *

from apps.formularios.usuarioForm import SignUpForm

class RegistrarUsuario(CreateView):
    model = User
    template_name = 'tienda/registrarUsuario.html'
    form_class = SignUpForm
    success_url = reverse_lazy('producto:mostrar_inicio')
    #return self.render_to_response(self(form = form))
#     def form_valid(self, form):
#         '''
#         En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
#         '''
#         form.save()
#         usuario = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         usuario = authenticate(username=usuario, password=password)
#         login(self.request, usuario)
#         return redirect('/')
#
# class BienvenidaView(TemplateView):
#    template_name = 'tienda/bienvenida.html'
