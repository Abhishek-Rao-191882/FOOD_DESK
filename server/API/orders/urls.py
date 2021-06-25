from django.contrib import admin
from django.urls import path
from . import views






urlpatterns = [
    # path('/',views.check, name='check'),

    path("seller_get_orders/<int:pk_value>/<int:type>", views.seller_orders.as_view(), name='seller_orders'),
    path("seller_get_orders/", views.seller_orders.as_view(), name='seller_orders')
]



