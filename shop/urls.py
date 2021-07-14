from django.urls import path, include
from rest_framework import routers

from shop.views import *


router = routers.DefaultRouter()
router.register('products', ProductsViewSet, basename='product')
router.register('shop', ShopViewSet, basename='shop')


urlpatterns = [
    path('', include(router.urls)),
    path('category/', ParentCategoryViewSet.as_view(), name='parent_category'),
    path('client/', ClientViewSet.as_view(), name='client'),
    path('client/<int:pk>', ClientViewSet.as_view(), name='client-detail')
]