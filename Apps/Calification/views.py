#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Calification
import json


#from django.shortcuts import render
# Create your views here.

#8 tabla Calification
class CalificationView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET /calification: recupera una lista de calification 
    #GET /calification/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            califications=list(Calification.objects.filter(id=id).values())
            if len(califications)>0: 
                datos={'message': "Success", 'califications': califications}
            else:
                datos={'message':'no data in the califications table'}
            return JsonResponse(datos)

        else:
            califications=list(Calification.objects.values())
            if len(califications)>0:
                datos={'message': "Success", 'Store': califications}
            else:
                datos={'message':'no data in the Store table'}
            return JsonResponse(datos)

    # POST /calification: crea un nuevo User 
    def post(self, request):
        jd=json.loads(request.body)
        Calification.objects.create(code=jd['code'],
                            califications=jd['califications'],
                            user_id=jd['user_id'],
                            store_id=jd['store_id'],)
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT /calification/1 - Actualiza la tabla calification # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        califications=list(Calification.objects.filter(id=id).values())
        if len(califications)>0:
            califications=Calification.objects.get(id=id)   
            califications.code=jd['code']
            califications.califications=jd['califications']
            califications.user_id=jd['user_id']
            califications.store_id=jd['store_id']
            califications.save()
            datos={'message': "Success"}
        else:
            datos={'message':'califications Update not found'}
        return JsonResponse(datos)
    
    # DELETE /calification/1 - Elimina el User enviandole el id #1 
    def delete(self, request, id):
        califications=list(Calification.objects.filter(id=id).values())
        if len(califications)>0:
            Calification.objects.filter(id=id).delete()   
            datos={'message': "Delete Store"}
        else:
            datos={'message': "Delete califications not found"}
        return JsonResponse(datos)


    
    
    
    
    
    
    