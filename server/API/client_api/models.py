from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.conf import settings
from seller_login.models import products

class Cart(models.Model):
    class Meta:
        verbose_name_plural = 'Cart'
    Product_Id = models.ForeignKey(products, on_delete=models.CASCADE)
    Client_Id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    # Created_On = models.DateTimeField()

    def __str__(self):
        return  self.Client_Id.first_name +' '+self.Client_Id.last_name  +' --> '+ self.Product_Id.Product_Name