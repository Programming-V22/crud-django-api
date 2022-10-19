#from gettext import Catalog
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
from passlib.hash import pbkdf2_sha256

#from django.shortcuts import render
# Create your views here.

#1 tabla user
class UserView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #GET / users: recupera una lista de users 
    #GET / users/1 - Recupera una lista específica (1)
    def get(self, request, id=0):
        if(id>0):
            users=list(User.objects.filter(id=id).values())
            if len(users)>0:
                #users=users[0] 
                datos={'message': "Success", 'Users': users}
            else:
                datos={'message':'no data in the users table'}
            return JsonResponse(datos)

        else:
            users=list(User.objects.values())
            if len(users)>0:
                datos={'message': "Success", 'Users': users}
            else:
                datos={'message':'no data in the User table'}
            return JsonResponse(datos)
        
     
    def post(self, request):
        jd=json.loads(request.body)
        User.objects.create(name=jd['name'],
                            lastname=jd['lastname'],
                            email=jd['email'],
                            password= pbkdf2_sha256.encrypt(jd['password']),
                            phone=jd['phone'],
                            birth=jd['birth'],
                            sex=jd['sex'])
        datos={'message': "Success"}
        return JsonResponse(datos)
            #return HttpResponse('')
            #return JsonResponse(datos)

            
    
          
 
    #PUT / User/1 - Actualiza la tabla User # 1
    def put(self, request, id):
        jd=json.loads(request.body)
        users=list(User.objects.filter(id=id).values())
        if len(users)>0:
            users=User.objects.get(id=id)   
            users.name=jd['name']
            users.lastname=jd['lastname']
            users.email=jd['email']
            users.password=jd['password']
            users.phone=jd['phone']
            users.birth=jd['birth']
            users.sex=jd['sex']
            users.save()
            datos={'message': "Success"}
        
        else:
            datos={'message':'users Update not found'}
        return JsonResponse(datos)
    
    # DELETE / users/1 - Elimina el User enviandole el id #1 
    def delete(self, request, id):
        users=list(User.objects.filter(id=id).values())
        if len(users)>0:
            User.objects.filter(id=id).delete()   
            datos={'message': "Delete User"}
        else:
            datos={'message': "Delete users not found"}
        return JsonResponse(datos)
    
    
""" if request.method=='POST':
    name=request.POST['name'],
    lastname=request.POST['lastname'],
    email=request.POST['email'],
    password=request.POST['password'],
    phone=request.POST['phone'],
    birth=request.POST['birth'],
    sex=request.POST['sex']
    
    encrip_password=pbkdf2_sha256.encrypt(request.POST['password'])"""