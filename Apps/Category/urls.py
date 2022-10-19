from django.urls import path
from .views import CategoryView

urlpatterns = [
    #3
    #al ingresar a api/category devuelve el metodo CategoryView, con un nombre de ubications_list
    path('category/', CategoryView.as_view(), name='product_list'),
    #al ingresar a api/category/1 devuelve el metodo CategoryView enviando un parametro(1) ubications_process
    path('category/<int:id>', CategoryView.as_view(), name='product_proccess'),
]
