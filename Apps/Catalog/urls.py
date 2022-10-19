from django.urls import path
from .views import CatalogView


urlpatterns = [
   
    #7
    #al ingresar a api/catalog devuelve el metodo CatalogView,
    path('catalog/', CatalogView.as_view(), name='catalog_list'),
    #al ingresar a api/catalog/1 devuelve el metodo CatalogView enviando un parametro(1) ubications_process
    path('catalog/<int:id>', CatalogView.as_view(), name='catalog_proccess')
    
    
]
