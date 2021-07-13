from rest_framework import serializers

from shop.models import *


class ChildCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildCategory
        fields = ['id', 'name', 'descriptions']


class ParentCategorySerializer(serializers.ModelSerializer):
    child_category = ChildCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ParentCategory
        fields = ['id', 'name', 'descriptions', 'child_category']


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ProductsImage
        fields = ('__all__')


class ProductsSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = Products
        fields = ('__all__')


class ShopSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    parent_category = serializers.PrimaryKeyRelatedField(source='parent_category.name', read_only=True)
    child_category = serializers.PrimaryKeyRelatedField(source='child_category.name', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'descriptions', 'image', 'parent_category', 'child_category', 'date_add']


class UserShopSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()

    class Meta:
        model = Users
        fields = ['url', 'username', 'email', 'is_staff', 'is_seller', 'shop']




