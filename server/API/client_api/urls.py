from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
router =routers.DefaultRouter()
router.register('cart', viewset=views.CartView, basename='cart')
# router.register('cart/<user_id>', viewset=views.CartView, basename='cart')






urlpatterns = [
    path('', include(router.urls)),
    # path('check/',views.check, name='check'),
    path('login', obtain_auth_token, name='loginAPI'),
    path('products/', views.Products.as_view(), name='products'),
    path('search/', views.SearchView.as_view())
    # path('cart/', views.Cart.as_view, name='cart'),
    # path('login/',views.check, name='check'),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
