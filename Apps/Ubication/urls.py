from django.urls import path
from .views import UbicationView


urlpatterns = [
    #5
    #al ingresar a api/ubications devuelve el metodo UbicationView, 
    path('ubications/', UbicationView.as_view(), name='ubications_list'),
    #al ingresar a api/ubications/1 devuelve el metodo UbicationView enviando un parametro(1) ubications_process
    path('ubications/<int:id>', UbicationView.as_view(), name='ubications_proccess'),
]
