#from gettext import Catalog
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json


#from django.shortcuts import render
# Create your views here.

#2 tabla Producto
class ProductView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / product: recupera una lista de produt 
    #GET / product/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            products=list(Product.objects.filter(id=id).values())
            if len(products)>0:
                #products=products[0]   
                datos={'message': "Success", 'products': products}
            else:
                datos={'message':'no data in the products table'}
            return JsonResponse(datos)

        else:
            products=list(Product.objects.values())
            if len(products)>0:
                datos={'message': "Success", 'Product': products}
            else:
                datos={'message':'no data in the Product table'}
            return JsonResponse(datos)

    # POST / Product: crea un nuevo User 
    def post(self, request):
        jd=json.loads(request.body)
        Product.objects.create(name=jd['name'],
                                description=jd['description'],
                                price=jd['price'],
                                image=jd['image'],
                                status=jd['status'],
                                user_id=jd['user_id'],)
        datos={'message': "Success"}
        return JsonResponse(datos)
 
    #PUT / Product/1 - Actualiza la tabla Product # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        products=list(Product.objects.filter(id=id).values())
        if len(products)>0:
            products=Product.objects.get(id=id)   
            products.name=jd['name']
            products.description=jd['description']
            products.price=jd['price']
            products.image=jd['image']
            products.status=jd['status']
            products.user_id=jd['user_id']
            products.save()
            datos={'message': "Success"}
        else:
            datos={'message':'products Update not found'}
        return JsonResponse(datos)
    
    # DELETE / product/1 - Elimina el User enviandole el id #1 
    def delete(self, request, id):
        products=list(Product.objects.filter(id=id).values())
        if len(products)>0:
            Product.objects.filter(id=id).delete()   
            datos={'message': "Delete Product"}
        else:
            datos={'message': "Delete products not found"}
        return JsonResponse(datos)

