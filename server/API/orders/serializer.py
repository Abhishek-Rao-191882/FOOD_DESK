from rest_framework import serializers

from .models import Orders_Id, Orders, Ordered_Product
from django.contrib.auth import get_user_model
from accounts.serializer import ClientSerializer


# For Registration Of Orders

class Orders_Id_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders_Id
        fields = ['Order_ID','TXN_ID','User_Id','Mobile','Address','Payment_Status','Total_Amount']


class Ordered_Products_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered_Product
        fields = ['Orders_ID','Product_Name','Product_Price','Product_Category','Product_Id']


class Orders_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['Orders_ID','Product','Quantity','Seller_Id','OTP','Total_Amount']




# For Seller to get Orders





class Seller_Order_Info_Get_Serializer(serializers.ModelSerializer):
    User_Id = ClientSerializer()
    class Meta:
        model = Orders_Id
        fields = ['User_Id','Mobile','Address',]


class Seller_Order_Product_Get_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered_Product
        fields = ['Product_Name', 'Product_Price', 'Product_Category','Product_Id']


class Seller_Get_Orders(serializers.ModelSerializer):
    Orders_ID = Seller_Order_Info_Get_Serializer(read_only=True)
    Product = Seller_Order_Product_Get_Serializer(read_only=True)
    class Meta:
        model = Orders
        fields = ['id','Orders_ID','Product','Quantity','Total_Amount','Date_Time','Delivery_Status']




    # Orders_ID = models.ForeignKey(Orders_Id, on_delete=models.CASCADE)
    # Product = models.OneToOneField(Ordered_Product, on_delete=models.CASCADE)
    # Quantity = models.PositiveSmallIntegerField()
    # # Seller_Id = models.PositiveSmallIntegerField()
    # Seller_Id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # OTP = models.PositiveSmallIntegerField()
    # Total_Amount = models.PositiveSmallIntegerField()
    # Date_Time = models.DateTimeField(auto_now_add=True)
    # Delivery_Status = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=False)
