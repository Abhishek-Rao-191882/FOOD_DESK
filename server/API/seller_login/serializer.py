from rest_framework import serializers
from .models import products, categories
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

# from .models import client
from django.contrib.auth.models import User, auth

# class SellerUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = client
#         fields = ['id','username','password']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = "__all__"



class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ['Category_Name']




from accounts.serializer import UserSerializer, HotelNameSerializer

class ProductsGetSerializer(serializers.ModelSerializer):
    Seller = HotelNameSerializer()
    Category = CategoryGetSerializer()
    class Meta:
        model = products
        fields = ['id','Product_Name','Price','Category','Seller','Image']



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = "__all__"




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id','username','first_name','last_name','email']
