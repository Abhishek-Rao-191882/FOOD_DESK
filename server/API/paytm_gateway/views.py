from django.shortcuts import render

# Create your views here.
from . import Checksum
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from  paytm_gateway.utils import VerifyPaytmResponse
import requests




from orders.models import Ordered_Product, Orders, Orders_Id
from orders.serializer import Orders_Id_Serializer, Ordered_Products_Serializer, Orders_Serializer
from random import randint





# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def home(request):
    # return Response(template_name='payment.html')

    # return render(request, "payment.html")
    return HttpResponse("<html><a href='http://localhost:8000/paytm_gateway/payment/'>PayNow</html>")
    # return Response('http://localhost:8000/payment',status=status.HTTP_200_OK)

# @api_view(('POST',))
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

import json


@csrf_exempt
@api_view(('GET','POST'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def payment(request):
    order_id = Checksum.__id_generator__()
    # bill_amount = str(request.data['amount'])
    # bill_amount = request.POST['amount']

    # print(request.POST)
    # front = json.loads(request.POST)
    front = request.POST
    mobile = front['mobile']
    address = front['address']
    bill_amount = str(front['amount'])
    orders = json.loads(front['order_items'])
    client_id = orders[0]['Client_Id']
    # print(type(client_id))
    txn_id = -1
    payment_status = False



    data_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        'MOBILE_NO': '7777777777',
        'EMAIL': 'arao8732@gmail.com',
        'CUST_ID': '123123',
        'ORDER_ID':order_id,
        'TXN_AMOUNT': bill_amount,
    } # This data should ideally come from database

    # txn = Orders_Id.objects.filter(TXN_ID__lte=-1)
    # txn.objects.filter().delete()


    order_id_table_id = order_id_table(order_id,txn_id,client_id,mobile,address,payment_status,bill_amount)
    OTP = randint(1000,9999)
    for product in orders:
        order_products_table_id = ordered_products(product, order_id_table_id)
        quantity = product['Quantity']
        seller = product['Product_Id']['Seller']['id']
        product_total_amount = product['Product_Id']['Price']*quantity
        orders_db(order_id_table_id,order_products_table_id,quantity,seller,OTP,product_total_amount)


    # delete all values with negative integer
    #save entries



    data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)
    context = {
        'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
        'comany_name': settings.PAYTM_COMPANY_NAME,
        'data_dict': data_dict
    }
    print(context)
    return render(request, 'payment.html', context)




def order_id_table(order_id,txn_id,client_id,mobile,address,payment_status,amount):
    datas = {
        'Order_ID': order_id,
        'TXN_ID': txn_id,
        'User_Id': client_id,
        'Mobile': mobile,
        'Address': address,
        'Payment_Status': payment_status,
        'Total_Amount': amount,
    }
    serialized = Orders_Id_Serializer(data = datas)
    if serialized.is_valid():
        orders_id_table = serialized.save()
        return orders_id_table.id;
    return None;


def ordered_products(products, order_id_table_id):
    datas = {
        'Orders_ID': order_id_table_id,
        'Product_Name': products['Product_Id']['Product_Name'],
        'Product_Price': products['Product_Id']['Price'],
        'Product_Category': products['Product_Id']['Category']['Category_Name'],
        'Product_Id': products['Product_Id']['id'],
    }
    serialized = Ordered_Products_Serializer(data=datas)
    if serialized.is_valid():
        orders_products_table = serialized.save()
        return orders_products_table.id;
    return None;




def orders_db(order_id_table_id,order_products_table_id,quantity,seller,OTP,product_total_amount):
    datas = {
        'Orders_ID': order_id_table_id,
        'Product': order_products_table_id,
        'Quantity': quantity,
        'Seller_Id': seller,
        'OTP': OTP,
        'Total_Amount': product_total_amount,
    }
    serialized = Orders_Serializer(data=datas)
    if serialized.is_valid():
        orders_table = serialized.save()
        return True;

    return None;




@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    print(resp)
    # fill transaction id

    txn_id = resp['paytm']['TXNID']
    bank_txn_id =  resp['paytm']['BANKTXNID']
    order_id = resp['paytm']['ORDERID']
    txn_amt = resp['paytm']['TXNAMOUNT']
    status = resp['paytm']['STATUS']
    bank_name = resp['paytm']['BANKNAME']
    txn_date = resp['paytm']['TXNDATE']
    # delete all values with negative integer
    if resp['verified']:

        order = Orders_Id.objects.get(Order_ID = order_id)
        order.Payment_Status = True
        order.TXN_ID = txn_id
        order.save()
        # save success details to db; details in resp['paytm']

        ss =2
        print("Success Payment API response")

        return redirect("http://localhost:8080/transaction_status?t_id="+str(txn_id)+"&bt_id="+str(bank_txn_id)+"&o_id="+str(order_id)+"&t_amt="+str(txn_amt)+"&sts="+str(status)+"&b_name="+str(bank_name)+"&t_date="+str(txn_date))


    else:
        print("Failed Payment API response")
        # check what happened; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)
