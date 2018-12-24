from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=20)
    descripcionCategoria = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return '%s' % self.nombreCategoria

class Proveedor(models.Model):
    tipoDocumentoProveedor = models.CharField(max_length=20)
    numeroDocumentoProveedor = models.CharField(max_length=11)
    nombreProveedor = models.CharField(max_length=50)
    direccionProveedor = models.CharField(max_length=50)
    telefonoProveedor = models.CharField(max_length=9)
    webProveedor = models.URLField()
    def __str__(self):
        return '%s' % self.nombreProveedor

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    precioProducto = models.FloatField(blank=True,default=0)
    precioOfertaProducto = models.FloatField(blank=True,default=0)
    tallaProducto = models.CharField(max_length=5)
    colorProducto = models.CharField(max_length=20)
    tipoProducto = models.CharField(max_length=20)
    marcaProducto = models.CharField(max_length=50)
    imagenProducto = models.ImageField()
    descripcionProducto = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    def __str__(self):
        return '%s' % self.nombreProducto

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'Perfiles de Usuario'


class Lote(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    tipoComprobante = models.CharField(max_length=7)
    nroComprobante = models.CharField(max_length=20)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)  # Field name made lowercase.

class Producto_lote(models.Model):
    cantidad = models.IntegerField()
    cantidadinicial = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)  # Field name made lowercase.
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)  # Field name made lowercase.
