from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username','first_name','last_name','email']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name']


class ClientInfo(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserInfo
        fields = ['Mobile_No','address','user']






class HotelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','first_name','last_name']