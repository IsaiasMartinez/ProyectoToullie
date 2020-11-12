from django.urls import path
from . import views

urlpatterns = [
    path('registro',views.registro, name='registro'),
    path('home',views.home, name='home'),                                                                               
    path('producto',views.producto, name='producto'),

    
    
    
    

]