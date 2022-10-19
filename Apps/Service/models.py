from django.db import models
from ..User.models import User
# Create your models here.
#4
class Service(models.Model):
    name = models.CharField(max_length=50)
    experience = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.