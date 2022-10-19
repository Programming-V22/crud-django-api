#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Store
import json


#from django.shortcuts import render
# Create your views here.

#6 tabla Store
class StoreView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / store: recupera una lista de store 
    #GET / store/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            stores=list(Store.objects.filter(id=id).values())
            if len(stores)>0: 
                datos={'message': "Success", 'stores': stores}
            else:
                datos={'message':'no data in the stores table'}
            return JsonResponse(datos)

        else:
            stores=list(Store.objects.values())
            if len(stores)>0:
                datos={'message': "Success", 'Store': stores}
            else:
                datos={'message':'no data in the Store table'}
            return JsonResponse(datos)

    # POST /store: crea un nuevo User 
    def post(self, request):
        jd=json.loads(request.body)
        Store.objects.create(frompage=jd['frompage'],
                            name=jd['name'],
                            description=jd['description'],
                            user_id=jd['user_id'],)
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT /store/1 - Actualiza la tabla Store # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        stores=list(Store.objects.filter(id=id).values())
        if len(stores)>0:
            stores=Store.objects.get(id=id)   
            stores.frompage=jd['frompage']
            stores.name=jd['name']
            stores.description=jd['description']
            stores.user_id=jd['user_id']
            stores.save()
            datos={'message': "Success"}
        else:
            datos={'message':'stores Update not found'}
        return JsonResponse(datos)
    
    # DELETE /store/1 - Elimina el User enviandole el id #1 
    def delete(self, request, id):
        stores=list(Store.objects.filter(id=id).values())
        if len(stores)>0:
            Store.objects.filter(id=id).delete()   
            datos={'message': "Delete Store"}
        else:
            datos={'message': "Delete stores not found"}
        return JsonResponse(datos)
