from django.contrib import admin
from shop.models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_fields = ('__all__')
    list_display = ['name']


@admin.register(Users)
class ShopUserAdmin(admin.ModelAdmin):
    list_fields = ('__all__')
    list_display = ['username', 'shop']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_fields = ('__all__')
    list_display = ['name', 'price']


@admin.register(ProductsImage)
class ProductsImageAdmin(admin.ModelAdmin):
    list_fields = ('__all__')


@admin.register(ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    list_fields = ('__all__')


@admin.register(ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_fields = ('__all__')