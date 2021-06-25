
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('payment/', views.payment),
    path('response/', views.response),
    # path('admin/', admin.site.urls),
]