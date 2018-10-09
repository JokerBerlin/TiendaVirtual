from django.db import models

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
    stockProducto = models.IntegerField()
    imagenProducto = models.ImageField()
    descripcionProducto = models.CharField(max_length=200)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    def __str__(self):
        return '%s' % self.nombreProducto
