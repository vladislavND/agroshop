from django.shortcuts import render
from rest_framework import routers, viewsets, views, generics

from shop.models import *
from shop.serializers import UserShopSerializer, ProductsSerializer, ParentCategorySerializer, ShopSerializer


class ParentCategoryApi(generics.ListAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer


class ProductsViewSet(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ShopUserViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = UserShopSerializer





