from django.db import models
from ..Product.models import Product
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    rangomin = models.IntegerField(blank=True, null=True)
    rangomax = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)  # Field name made lowercase.
