from django.contrib import admin

# Register your models here.
from .models import Orders_Id, Orders, Ordered_Product



class Orders_id(admin.ModelAdmin):
    list_display = ['Order_ID','TXN_ID','User_Id','Mobile','Address','Date_Time','Payment_Status','Total_Amount','Refund_Amount']

admin.site.register(Orders_Id, Orders_id)

class orders(admin.ModelAdmin):
    list_display = ['Orders_ID','Product','Quantity','Seller_Id','OTP','Total_Amount','Date_Time','Delivery_Status','Acceptance_Status']
    # list_display_links = ('Orders_Id',)
    list_filter = ('Date_Time','Delivery_Status','Acceptance_Status','Seller_Id')
    search_fields = ['Orders_Id__Order_ID','Orders_Id__User_Id__email',]


admin.site.register(Orders, orders)

class ordered_products(admin.ModelAdmin):
    list_display = ['Product_Name','Orders_ID','Product_Price','Product_Category','Product_Id']

admin.site.register(Ordered_Product, ordered_products)