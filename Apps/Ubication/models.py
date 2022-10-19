from django.db import models

# Create your models here.
#5   
class Ubication(models.Model):
    code = models.CharField(max_length=255)
    tipe = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=250)