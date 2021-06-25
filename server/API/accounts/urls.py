from django.contrib import admin
from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token



from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sign_up/', views.sign_up.as_view(), name='Sign_Up'),
    path('login', obtain_auth_token, name='loginAPI'),
    path('update_client_info', views.update_client_info.as_view(), name='Update_Client_Info'),
    path('clientlogin', views.ClientLogin.as_view(), name='Client_Login'),
    path('sellerlogin', views.SellerLogin.as_view(), name='Seller_Login'),
    path('logout', views.logout.as_view(), name='loginAPI'),




    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),

]
