from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import products, categories
# Create your views here.
# from .serializer import SellerLoginSerializer
from .serializer import ProductsSerializer, ProductsGetSerializer,CategorySerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from .forms import LoginForm

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    # return render(request, 'test.html')
    return Response({'msg':'hello tokens'})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Authentication

from rest_framework.views import APIView

# from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
# class SellerLogin(APIView):
#     # permission_classes = [IsAuthenticated]
#     # authentication_classes = [TokenAuthentication]
#
#     def post(self, request):
#         data = request.data
#         try:
#             token = Token.objects.get(key=data['token']).key
#             user = Token.objects.get(key=data['token']).user
#             # print(user.first_name)
#             print(user.is_superuser)
#             if user.is_superuser:
#                 serialzed = UserSerializer(user)
#                 # print(serialzed.data)
#                 print("success login")
#                 return Response(serialzed.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#             # return Response({"msg":"Only Hotels Are Allowed"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#         except:
#             return Response("Token Failed to login", status=status.HTTP_400_BAD_REQUEST)
#             # print(token)
#
#             # user = auth.authenticate(username=data['username'],password=data['password'])
#             # if user is not None:
#             #     if user.is_superuser:
#             #             auth.login(request,user)
#             #             return Response("Success Login 2", status = status.HTTP_200_OK)
#             #     else:
#             #         return Response("For Active Users Only", status= status.HTTP_403_FORBIDDEN)
#             return Response({"loginstatus":"Fail To Login"}, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         return Response("Method Not Acceptable", status=status.HTTP_401_UNAUTHORIZED)
#
#
# class logout(APIView):
#     def post(self, request):
#         data = request.data
#         # print(data)
#         # simply delete the token to force a login
#         Token.objects.get(key=data['token']).delete()
#         # request.user.auth_token.delete()
#
#         return Response(status=status.HTTP_200_OK)

from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
class ProductsView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser)

    def get_object(self, pk):
        try:
            return products.objects.get(pk=pk)
        except products.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def get(self, *args, **kwargs):
            # print(self.kwargs['pk'])
            id = self.kwargs['pk']
            ss = products.objects.all().filter(Seller=id)
            datas = ProductsGetSerializer(ss, many=True)
            # print(datas.data[1])
            return Response(datas.data, status=status.HTTP_200_OK)
        # except:
            # return Response("Sorry", status=status.HTTP_200_OK)

    def post(self, request):
        # print(request.data)
        # print("sss")
        # print(request.data)
        serializer = ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("failed here")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        # print("Inside PUT")
        update = self.get_object(pk)
        # print("Inside PUT2")
        # print(update.Image)
        # print(request.data['Seller'])
        if request.data['Image']== 'undefined':
            request.data._mutable = True
            request.data['Image'] = update.Image
            request.data._mutable = False
        serializer = ProductsSerializer(update, data=request.data)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # print(self.get_object(pk))
        dele = self.get_object(pk)
        dele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductsOperationView(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = ProductsSerializer





class CategoriesGetView(APIView):

    def post(self, request):
        data = request.data
        try:
            # token = Token.objects.get(key=data['token']).key
            # user = Token.objects.get(key=data['token']).user
            Userid = data['userId']
            # print(Userid)
            # print(request.data)
            categ = categories.objects.all().filter(Seller=Userid)
            categSerialized = CategorySerializer(categ, many=True)
            # print(categSerialized.data)
            # if categSerialized.is_valid():
            #     categSerialized.save()
                # print(categSerialized.data)
            return Response(categSerialized.data, status=status.HTTP_200_OK)
        except:
            return Response("Token Failed to login", status=status.HTTP_400_BAD_REQUEST)

class CategoriesOperationView(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = CategorySerializer
    # def get_queryset(self,**kwargs,):
    #     return categories.objects.all().filter(Seller=21)
