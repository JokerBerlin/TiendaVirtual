from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from apps.models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude={}

        labels = {
            'nombreProducto': 'Nombre producto',
            'precioProducto': 'Precio de producto',
            'precioOfertaProducto': 'Precio de oferta del producto',
            'taleProducto': 'Talla de producto',
            'colorProducto': 'Color del producto',
            'tipoProducto': 'Tipo de producto',
            'marcaProducto': 'Marca del producto',
            'imagenProducto': 'Imagen del producto',
            'descripcionProducto': 'Descripción del producto',
            'categoria': 'Categoria',


        }

        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'precioProducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'precioOfertaProducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'tallaProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'colorProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'marcaProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'imagenProducto': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcionProducto': forms.Textarea(attrs={'class': 'form-control','height':'50px','cols':"40", 'rows':"3", 'style':"resize: both",}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
