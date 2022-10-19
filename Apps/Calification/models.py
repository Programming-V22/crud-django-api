from django.db import models
from ..User.models import User
from ..Store.models import Store
# Create your models here.
#8
class Calification(models.Model):
    code = models.IntegerField()
    califications = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)  # Field name made lowercase.