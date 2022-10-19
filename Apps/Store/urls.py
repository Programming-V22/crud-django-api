from django.urls import path
from .views import StoreView


urlpatterns = [
    #6
    #al ingresar a api/store devuelve el metodo StoreView,
    path('store/', StoreView.as_view(), name='service_list'),
    #al ingresar a api/store/1 devuelve el metodo StoreView enviando un parametro(1) ubications_process
    path('store/<int:id>', StoreView.as_view(), name='service_proccess'),
    
]