from rest_framework import serializers

from .models import Cart
from seller_login.serializer import ProductsGetSerializer, CategoryGetSerializer
from accounts.serializer import HotelNameSerializer


from django.contrib.auth import get_user_model


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','Product_Id','Client_Id','Quantity']

class CartReadSerializer(serializers.ModelSerializer):
    Product_Id = ProductsGetSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id','Product_Id','Client_Id','Quantity']