#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Catalog
import json


#from django.shortcuts import render
# Create your views here.

#7 table catalog
# si se quiere borrar un catalog no tiene que aver ningun producto en el catalogo ni store
class CatalogView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / catalog: recupera una lista de catalogs 
    #GET / catalog/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            catalogs=list(Catalog.objects.filter(id=id).values())
            if len(catalogs)>0:
                #catalogs=catalogs[0]   
                datos={'message': "Successss", 'Catalog': catalogs}
            else:
                datos={'message':'no data in the Catalog table'}
            return JsonResponse(datos)
        else:
            catalogs=list(Catalog.objects.values())
            if len(catalogs)>0:
                datos={'message': "Success", 'Catalog': catalogs}
            else:
                datos={'message':'no data in the Catalog table'}
            return JsonResponse(datos)
        
    # POST /catalog: crea un nueva Ubication ingresando el tambien el id
    def post(self, request):
        jd=json.loads(request.body)
        Catalog.objects.create(store_id=jd['store_id'],
                               product_id=jd['product_id'])
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT /catalog/1 - Actualiza la tabla Catalog # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        catalogs=list(Catalog.objects.filter(id=id).values())
        if len(catalogs)>0:
            catalogs=Catalog.objects.get(id=id) 
            catalogs.store_id=jd['store_id']
            catalogs.product_id=jd['product_id']
            catalogs.save()
            datos={'message': "Success"}
        else:
            datos={'message':'catalogs Update not found'}
        return JsonResponse(datos)
    
    # DELETE /catalog/1 - Elimina el Catalog  enviandole el id #1 
    def delete(self, request, id):
        catalogs=list(Catalog.objects.filter(id=id).values())
        if len(catalogs)>0:
            Catalog.objects.filter(id=id).delete()   
            datos={'message': "Delete Catalog"}
        else:
            datos={'message': "Delete Catalog not found"}
        return JsonResponse(datos)
