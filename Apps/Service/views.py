#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Service
import json


#from django.shortcuts import render
# Create your views here.

#4 tabla Service
class ServiceView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / service: recupera una lista de produt 
    #GET / service/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            services=list(Service.objects.filter(id=id).values())
            if len(services)>0:
                #services=services[0]   
                datos={'message': "Success", 'services': services}
            else:
                datos={'message':'no data in the services table'}
            return JsonResponse(datos)

        else:
            services=list(Service.objects.values())
            if len(services)>0:
                datos={'message': "Success", 'service': services}
            else:
                datos={'message':'no data in the service table'}
            return JsonResponse(datos)

    # POST / service: crea un nuevo User 
    def post(self, request):
        jd=json.loads(request.body)
        Service.objects.create(name=jd['name'],
                                experience=jd['experience'],
                                user_id=jd['user_id'],)
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT / service/1 - Actualiza la tabla service # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        services=list(Service.objects.filter(id=id).values())
        if len(services)>0:
            services=Service.objects.get(id=id)
            services.name=jd['name']
            services.experience=jd['experience']
            services.user_id=jd['user_id']
            services.save()
            datos={'message': "Success"}
        else:
            datos={'message':'services Update not found'}
        return JsonResponse(datos)
    
    # DELETE / service/1 - Elimina el User enviandole el id #1 
    def delete(self, request, id):
        services=list(Service.objects.filter(id=id).values())
        if len(services)>0:
            Service.objects.filter(id=id).delete()   
            datos={'message': "Delete service"}
        else:
            datos={'message': "Delete service not found"}
        return JsonResponse(datos)
        