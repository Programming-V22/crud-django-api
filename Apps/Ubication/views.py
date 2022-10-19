#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Ubication
import json


#from django.shortcuts import render
# Create your views here.

#5 table ubication
class UbicationView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / ubications: recupera una lista de ubications 
    #GET / ubications/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            ubications=list(Ubication.objects.filter(id=id).values())
            if len(ubications)>0:
                #ubications=ubications[0]   
                datos={'message': "Successss", 'Ubication': ubications}
            else:
                datos={'message':'no data in the location table'}
            return JsonResponse(datos)

        else:
            ubications=list(Ubication.objects.values())
            if len(ubications)>0:
                datos={'message': "Success", 'Ubication': ubications}
            else:
                datos={'message':'no data in the location table'}
            return JsonResponse(datos)
        
    # POST / Ubication: crea un nueva Ubication ingresando el tambien el id
    def post(self, request):
        jd=json.loads(request.body)
        Ubication.objects.create(code=jd['code'], tipe=jd['tipe'], date=jd['date'],latitude=jd['latitude'],longitude=jd['longitude'])
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT / Ubication/1 - Actualiza la tabla Ubication # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        ubications=list(Ubication.objects.filter(id=id).values())
        if len(ubications)>0:
            ubications=Ubication.objects.get(id=id)   
            ubications.code=jd['code']
            ubications.tipe=jd['tipe']
            ubications.date=jd['date']
            ubications.latitude=jd['latitude']
            ubications.longitude=jd['longitude']
            ubications.save()
            datos={'message': "Success"}
        else:
            datos={'message':'ubications Update not found'}
        return JsonResponse(datos)
    
    # DELETE / Ubications/1 - Elimina la Ubicacion  enviandole el id #1 
    def delete(self, request, id):
        ubications=list(Ubication.objects.filter(id=id).values())
        if len(ubications)>0:
            Ubication.objects.filter(id=id).delete()   
            datos={'message': "Delete ubication"}
        else:
            datos={'message': "Delete ubications not found"}
        return JsonResponse(datos)
