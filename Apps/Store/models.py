from django.db import models
from ..User.models import User
# Create your models here.
#6
class Store(models.Model):
    frompage = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)
    #ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.