from django.urls import path
from .views import ProductView


urlpatterns = [
   
    #2
    #al ingresar a api/product devuelve el metodo ProductView, con un nombre de ubications_list
    path('product/', ProductView.as_view(), name='product_list'),
    #al ingresar a api/product/1 devuelve el metodo ProductView enviando un parametro(1) ubications_process
    path('product/<int:id>', ProductView.as_view(), name='product_proccess')
    
   
]
