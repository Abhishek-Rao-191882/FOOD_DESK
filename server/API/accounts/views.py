from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import UserInfo
from .serializer import ClientInfo, ClientSerializer, UserSerializer


from django.shortcuts import render
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm

class update_client_info(APIView):

    def put(self, request):
        user_model = get_user_model()
        user = user_model.objects.get(email=request.data['email'])
        if user:
             U_info = UserInfo.objects.get(user= user.id)
             try:
                 user.first_name = request.data['first_name']
                 user.last_name = request.data['last_name']
                 U_info.Mobile_No = request.data['Mobile_No']
                 U_info.address = request.data['address']
                 user.save()
                 U_info.save()
             except:
                 return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
        return Response("Updated", status=status.HTTP_200_OK)

class sign_up(APIView):

    def post(self, request):
        try:
            user_model = get_user_model()
            user = user_model.objects.get(email=request.data['email'])
            return Response('User Already Exist', status=status.HTTP_400_BAD_REQUEST)
        except:
            print('ok'+str(request.data))

            user = user_model.objects.create_user(email=request.data['email'],password=request.data['password'],first_name = request.data['first_name'],last_name = request.data['last_name'])
            user.is_active = False
            user.save()
            sendConfirm(user)
            # print(type(user))
            client = ClientSerializer(user)
            # print(type(client))
            mobile= request.data['mobile']
            address = request.data['address']

            UInfo = UserInfo(Mobile_No = mobile, address = address, user = user)
            UInfo.save()
            print(type(UInfo))
            clientIn = ClientInfo(UInfo)
            print(type(ClientInfo))
            # print(UInfo)
            # print(client)
            # print(clientIn)


            return Response(client.data, status=status.HTTP_200_OK)





    def get(self, *args, **kwargs):
        print("done")
        return Response('Ok', status=status.HTTP_200_OK)




class SellerLogin(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data
        try:
            token = Token.objects.get(key=data['token']).key
            user = Token.objects.get(key=data['token']).user
            # print(user.first_name)
            # print(user.is_superuser)
            if user.is_superuser:
                serialzed = UserSerializer(user)
                return Response(serialzed.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            # return Response({"msg":"Only Hotels Are Allowed"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            return Response("Token Failed to login", status=status.HTTP_400_BAD_REQUEST)
            # print(token)

            # user = auth.authenticate(username=data['username'],password=data['password'])
            # if user is not None:
            #     if user.is_superuser:
            #             auth.login(request,user)
            #             return Response("Success Login 2", status = status.HTTP_200_OK)
            #     else:
            #         return Response("For Active Users Only", status= status.HTTP_403_FORBIDDEN)
            return Response({"loginstatus":"Fail To Login"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response("Method Not Acceptable", status=status.HTTP_401_UNAUTHORIZED)





class ClientLogin(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data
        try:
            token = Token.objects.get(key=data['token']).key
            user = Token.objects.get(key=data['token']).user
            print(user.is_superuser)
            if user.is_active:
                serialzed = UserSerializer(user)
                print(serialzed.data)
                info = UserInfo.objects.get(user = serialzed.data['id'])
                info_serialized = ClientInfo(info)
                print(info.address)
                # serialzed.update(info.address)
                # print(serialzed.data['id'])
                return Response(info_serialized.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            # return Response({"msg":"Only Hotels Are Allowed"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            return Response("Token Failed to login", status=status.HTTP_400_BAD_REQUEST)
            # print(token)

            # user = auth.authenticate(username=data['username'],password=data['password'])
            # if user is not None:
            #     if user.is_superuser:
            #             auth.login(request,user)
            #             return Response("Success Login 2", status = status.HTTP_200_OK)
            #     else:
            #         return Response("For Active Users Only", status= status.HTTP_403_FORBIDDEN)
            return Response({"loginstatus":"Fail To Login"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response("Method Not Acceptable", status=status.HTTP_401_UNAUTHORIZED)








class logout(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        # simply delete the token to force a login
        Token.objects.get(key=data['token']).delete()
        # request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)
