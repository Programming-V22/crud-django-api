from django.urls import path
from .views import CalificationView

urlpatterns = [

    #8
    #al ingresar a api/calification devuelve el metodo CalificationView,
    path('calification/', CalificationView.as_view(), name='calification_list'),
    #al ingresar a api/calification/1 devuelve el metodo CalificationView enviando un parametro(1) calification_process
    path('calification/<int:id>', CalificationView.as_view(), name='calification_proccess'),
]
