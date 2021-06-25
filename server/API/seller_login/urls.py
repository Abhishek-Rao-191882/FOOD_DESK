from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from rest_framework import routers
router =routers.DefaultRouter()
router.register('categoriesOperations', viewset=views.CategoriesOperationView, basename='categories')
router.register('productsOperations', viewset=views.ProductsOperationView, basename='product')
# router.register('login/<user_id>', viewset=views.login, basename='login')
# router.register('login', viewset=views.login, basename='login')

# urlpatterns = [
#     path('',include(router.urls))
# ]
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # path('login', views.login, name='login'),
    path('', include(router.urls)),
    # path('sellerlogin', views.SellerLogin.as_view(), name='classAPI'),
    # path('login', obtain_auth_token, name='loginAPI'),
    # path('logout', views.logout.as_view(), name='loginAPI'),
    path('classLogin/auth/', include('rest_framework.urls'), name='classAPI'),
    path('home', views.home, name='index'),
    path('products/<int:pk>', views.ProductsView.as_view(), name='product'),
    path('products', views.ProductsView.as_view(), name='product'),
    path('categories', views.CategoriesGetView.as_view(), name='product'),
    # path('categoriesop', views.CategoriesOperationView.as_view(), name='product')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
