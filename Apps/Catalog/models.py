from django.db import models
from ..Store.models import Store
from ..Product.models import Product
# Create your models here.
#7
class Catalog(models.Model):
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)  # Field name made lowercase., 
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)  # Field name made lowercase.