
from django.db import models

from passlib.hash import pbkdf2_sha256
# Create your models here.
#1
class User(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    #la contraseña debe ir con un length de 256 porque el hash asi esta con 256 ok!
    password = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()
    birth = models.DateField()
    sex = models.IntegerField()
    
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)