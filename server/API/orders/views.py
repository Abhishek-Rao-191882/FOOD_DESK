from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from .serializer import Seller_Get_Orders
from .models import Orders


class seller_orders(APIView):

    # def get_objects(self,pk_value):
    #     print(pk_value)

    def get(self, *args, **kwargs):
            id = self.kwargs['pk_value']
            type = self.kwargs['type']
            if type==0:
                orders = Orders.objects.all().filter(Seller_Id = id,Acceptance_Status='').order_by('id').reverse()
            elif type==1:
                orders = Orders.objects.all().filter(Seller_Id = id,Acceptance_Status=True).order_by('id').reverse()
            elif type==2:
                orders = Orders.objects.all().filter(Seller_Id = id,Acceptance_Status=False).order_by('id').reverse()
            else:
                return Response("Bad Request / Or Outsider Attempt", status=status.HTTP_400_BAD_REQUEST)


            if orders:
                order_serialized = Seller_Get_Orders(orders, many=True)
                return Response(order_serialized.data,status=status.HTTP_200_OK)
            else:
                return Response("Bad Request / Or Outsider Attempt", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serial_id= request.data['id']
        Seller_id= request.data['Seller_id']
        acceptance_status = bool(request.data['Acceptance_Status'])
        print(acceptance_status)
        try:
            order_detail = Orders.objects.all().filter(Seller_Id=Seller_id,id=serial_id).update(Acceptance_Status=acceptance_status)
            return Response("OK",status=status.HTTP_200_OK)
        except:
            return Response("Bad Request / Or Outsider Attempt",status=status.HTTP_400_BAD_REQUEST)