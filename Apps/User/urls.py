from django.urls import path
from .views import UserView

urlpatterns = [
    #1
    #al ingresar a api/user devuelve el metodo UserView, con un nombre de ubications_list
    path('user/', UserView.as_view(), name='user_list'),
    #al ingresar a api/user/1 devuelve el metodo UserView enviando un parametro(1) ubications_process
    path('user/<int:id>', UserView.as_view(), name='user_proccess'),
    
]