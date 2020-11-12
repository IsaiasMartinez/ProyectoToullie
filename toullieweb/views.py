from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.conf import settings
from toullieweb.models import Producto,Marca,Categoria



# Create your views here.
def registro(request):
    mensaje = ""
    lista = {}
    if request.method == "POST":
        rut         = request.POST["txtRut"]
        nombre      = request.POST["txtNombr"]
        apellido    = request.POST["txtApellido"]
        correo      = request.POST["txtCorreo"]
        clave       = request.POST["txtPass"]
        telefono    = request.POST["Telefono"]
        nacimiento  = request.POST["nacimiento"]
        User.objects.create(username= nombre, email=correo, password= make_password(clave))
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'registro.html', {})
    
def home(request):
    return render(request, 'plantillabase.html',{} )

def producto(request):
    mensaje = ""
    lista = {}
    item  = {}
    
    if request.method == "POST":
        id                  = int("0"+ request.POST["txtId"])
        codigo              = request.POST["txtCodigo"]
        descripcion         = request.POST["Descripcion"]
        stock               = request.POST["txtStock"]
        precioCosto         = request.POST["txtPrecioCosto"]
        precioVenta         = request.POST["txtPrecioVenta"]
       
        if 'btnEnviar' in request.POST:
            Producto.objects.create(codigo= codigo, descripcion= descripcion, stock= stock, precioCosto= precioCosto, precioVenta= precioVenta)
            mensaje= "la operacion fue exitosa"
        elif 'btnListarr' in request.POST:
            lista = Producto.objects.all()
        elif 'btnBuscar' in request.POST:
            try:
                item = Producto.objects.get(pk = id)
            except:
            
                mensaje = " Producto no encontrado"
                item={}
        elif 'btnDelete' in request.POST:
            item = Producto.objects.get(pk = id)
            
            if isinstance(item, Producto):
                item.delete()
                mensaje= "Producto eliminado"
                item={}
               
            
            
    contexto = {'mensaje': mensaje, 'lista' : lista, 'item' : item} 
    return render(request, 'producto.html', contexto)
    
















