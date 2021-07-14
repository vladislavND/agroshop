from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from shop.models import *
from shop.serializers import (
    ClientSerializer,
    ProductsSerializer,
    ParentCategorySerializer,
    ShopSerializer)
from shop.permissions import IsOwnerOrReadOnly


class ShopPagination(PageNumberPagination):
    page_size = 10


class ParentCategoryViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = ShopPagination


class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ClientViewSet(generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer





