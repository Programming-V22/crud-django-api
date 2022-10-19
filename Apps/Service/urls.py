from django.urls import path
from .views import ServiceView


urlpatterns = [
    #4
    #al ingresar a api/service devuelve el metodo ServiceView, con un nombre de ubications_list
    path('service/', ServiceView.as_view(), name='service_list'),
    #al ingresar a api/service/1 devuelve el metodo ServiceView enviando un parametro(1) ubications_process
    path('service/<int:id>', ServiceView.as_view(), name='service_proccess'),

]
