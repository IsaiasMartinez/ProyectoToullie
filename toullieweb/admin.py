from django.contrib import admin
from .models import Producto
from .models import Categoria
from .models import Marca
# Register your models here.
class administradorProducto(admin.ModelAdmin):
	list_display 		= ['precioVenta','codigo', 'descripcion','stock']
	list_filter	 		= ['descripcion']
	search_fields		= ['descripcion', 'codigo']
	list_display_links 	= ['descripcion', 'codigo']
admin.site.register(Producto, administradorProducto)

class administradorCategoria(admin.ModelAdmin):
	list_display 		= ['nombre','activo']
	list_filter	 		= ['nombre']
	search_fields		= ['nombre', 'activo']
	list_display_links 	= ['nombre', 'activo']
admin.site.register(Categoria, administradorCategoria)

class administradorMarca(admin.ModelAdmin):
	list_display 		= ['nombre','activo']
	list_filter	 		= ['nombre']
	search_fields		= ['nombre', 'activo']
	list_display_links 	= ['nombre', 'activo']
admin.site.register(Marca,administradorMarca)




