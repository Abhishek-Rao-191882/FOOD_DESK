from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def check(request):
#     return HttpResponse('Hello')
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import filters

from seller_login.models import products, categories
from seller_login.serializer import ProductsGetSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Cart
from .serializer import CartSerializer, CartReadSerializer

from accounts.serializer import UserSerializer

# @api_view(('GET',))
# def Products(request):
#     # ss = categories.
#     user_model = get_user_model()
#     # ss = user_model.objects.get(id=21).categories_set.all()
#     ss = products.objects.all()
#     # datas = UserSerializer(ss, many=True)
#     datas = ProductsGetSerializer(ss, many=True)
#     # datas = CategorySerializer(ss, many=True)
#     # print(datas.data[1])
#     return Response(datas.data, status=status.HTTP_200_OK)


class ProductsPagination(PageNumberPagination):
    page_size = 2



class Products(ListAPIView):
    queryset = products.objects.all()
    serializer_class = ProductsGetSerializer
    pagination_class = ProductsPagination
    # http_method_names = ['POST']



class CartView(viewsets.ModelViewSet):
    # serializer_class = CartSerializer
    # queryset = Cart.objects.all()
    # pagination_class = None
    def get_queryset(self):
        if self.request.method in ['GET']:
            user_id = self.request.query_params.get("user_id", None)
            queryset = Cart.objects.all().filter(Client_Id=user_id)
            return queryset

        else:
            queryset = Cart.objects.all()
            return queryset


    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return CartReadSerializer

        return CartSerializer

# class SearchView(ListAPIView):
#     queryset = products.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']

class SearchView(ListAPIView):
    queryset = products.objects.all()
    serializer_class = ProductsGetSerializer
    search_fields = ['Product_Name','Category__Category_Name','Seller__first_name','Seller__last_name',]
    filter_backends = (filters.SearchFilter,)
    # search_fields = ['question_text']
    # filter_backends = (filters.SearchFilter,)
