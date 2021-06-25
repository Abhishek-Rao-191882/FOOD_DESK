from django.db import models
from django.conf import settings



# Create your models here.


from django.contrib.auth import get_user_model

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
class Orders_Id(models.Model):
    Order_ID = models.CharField(max_length=200)
    TXN_ID = models.CharField(max_length=200,default=-1)
    User_Id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET('Deleted'),blank=False)
    Mobile = models.BigIntegerField(default=9999999999)
    Address = models.CharField(max_length=1000)
    Date_Time = models.DateTimeField(auto_now_add=True,)
    Payment_Status = models.BooleanField(choices=TRUE_FALSE_CHOICES,default=False)
    Total_Amount = models.FloatField()
    Refund_Amount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.Order_ID
        # return self.Order_ID+' '+str(self.User_Id)




class Ordered_Product(models.Model):
    Orders_ID = models.ForeignKey(Orders_Id,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=130)
    Product_Price = models.PositiveSmallIntegerField()
    Product_Category = models.CharField(max_length=80)
    Product_Id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.Product_Name)




class Orders(models.Model):
    Orders_ID = models.ForeignKey(Orders_Id,on_delete=models.CASCADE)
    Product = models.OneToOneField(Ordered_Product,on_delete=models.CASCADE)
    Quantity = models.PositiveSmallIntegerField()
    # Seller_Id = models.PositiveSmallIntegerField()
    Seller_Id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    OTP = models.PositiveSmallIntegerField()
    Total_Amount = models.PositiveSmallIntegerField()
    Date_Time = models.DateTimeField(auto_now_add=True)
    Delivery_Status = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=False)
    Acceptance_Status = models.BooleanField(choices=TRUE_FALSE_CHOICES, default="", null=True)

    def __str__(self):
        return str(self.Orders_ID)+' '+str(self.Product)
