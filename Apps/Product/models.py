from django.db import models
from ..User.models import User
# Create your models here.
#2    
class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.CharField(max_length=50)
    status = models.CharField(max_length=45)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    def __str__(self):
        return self.title + '-' + self.user.name