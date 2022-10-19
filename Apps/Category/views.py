#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Category
import json


#from django.shortcuts import render
# Create your views here.

#3 tabla Category
class CategoryView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / category: recupera una lista de produt 
    #GET / category/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            categorys=list(Category.objects.filter(id=id).values())
            if len(categorys)>0:
                #categorys=categorys[0]   
                datos={'message': "Success", 'categorys': categorys}
            else:
                datos={'message':'no data in the categorys table'}
            return JsonResponse(datos)

        else:
            categorys=list(Category.objects.values())
            if len(categorys)>0:
                datos={'message': "Success", 'Category': categorys}
            else:
                datos={'message':'no data in the Category table'}
            return JsonResponse(datos)

    # POST / Category: crea un nuevo User 
    def post(self, request):
        jd=json.loads(request.body)
        Category.objects.create(name=jd['name'],
                                rangomin=jd['rangomin'],
                                rangomax=jd['rangomax'],
                                product_id=jd['product_id'],)
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT / category/1 - Actualiza la tabla category # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        categorys=list(Category.objects.filter(id=id).values())
        if len(categorys)>0:
            categorys=Category.objects.get(id=id)   
            categorys.name=jd['name']
            categorys.rangomin=jd['rangomin']
            categorys.rangomax=jd['rangomax']
            categorys.product_id=jd['product_id']
            categorys.save()
            datos={'message': "Success"}
        else:
            datos={'message':'categorys Update not found'}
        return JsonResponse(datos)
    
    # DELETE / category/1 - Elimina el User enviandole el id #1 
    def delete(self, request, id):
        categorys=list(Category.objects.filter(id=id).values())
        if len(categorys)>0:
            Category.objects.filter(id=id).delete()   
            datos={'message': "Delete Category"}
        else:
            datos={'message': "Delete categorys not found"}
        return JsonResponse(datos)
    
