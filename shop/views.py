from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination

from shop.models import *
from shop.serializers import UserShopSerializer, ProductsSerializer, ParentCategorySerializer, ShopSerializer


class ShopPagination(PageNumberPagination):
    page_size = 1


class ParentCategoryViewSet(generics.ListAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer


class ProductsViewSet(generics.ListAPIView, generics.UpdateAPIView,
                      generics.DestroyAPIView, generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = ShopPagination


class ShopUserViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class UserViewSet(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserShopSerializer





