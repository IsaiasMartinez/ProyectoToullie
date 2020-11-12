from django.db import models

# Create your models here.

        
        
class Categoria(models.Model):
    nombre      = models.TextField(max_length = 15)
    activo      = models.BooleanField()
    
    def __str__(self):
        return self.nombre
        
class Marca(models.Model):
    nombre      = models.TextField(max_length = 15)
    activo      = models.BooleanField()
    
    def __str__(self):
        return self.nombre
  
class Producto(models.Model):
    marca       = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.SET_NULL)
    categoria   = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    codigo      = models.DecimalField(max_digits=13, decimal_places=0)
    descripcion = models.TextField(max_length = 100)
    stock       = models.IntegerField()
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()
    
    def __str__(self):
        return self.descripcion

