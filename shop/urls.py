from django.urls import path, include
from rest_framework import routers

from shop.views import *


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('category/', ParentCategoryViewSet.as_view(), name='parent_category'),
    path('products/', ProductsViewSet.as_view(), name='products'),
    path('products/<int:pk>', ProductsViewSet.as_view(), name='detail_products'),
    path('shop/', ShopUserViewSet.as_view({'get': 'list'}), name='shop'),
    path('users/', UserViewSet.as_view(), name='users')
]