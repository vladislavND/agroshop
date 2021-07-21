from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from shop.models import *


class CountrySerializer(serializers.ModelSerializer):
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())

    class Meta:
        model = Country
        fields = ('__all__')


class RegionSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())

    class Meta:
        model = Region
        fields = ('__all__')


class CitySerializer(serializers.ModelSerializer):
    village = serializers.PrimaryKeyRelatedField(queryset=Village.objects.all())

    class Meta:
        model = City
        fields = ('__all__')


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ('__all__')


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
    image = ImageSerializer(many=True, required=False)
    sale_price = serializers.DecimalField(source='products_sale_price', max_digits=12, decimal_places=2, required=False)
    shop_name = serializers.CharField(source='shop.name', required=False)

    class Meta:
        model = Product
        fields = ('__all__')


class ShopSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    parent_category = serializers.PrimaryKeyRelatedField(queryset=ParentCategory.objects.all())
    child_category = serializers.PrimaryKeyRelatedField(queryset=ChildCategory.objects.all(), required=False)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=True)
    parent_category_name = serializers.CharField(source='parent_category.name', read_only=True)
    child_category_name = serializers.CharField(source='child_category.name', read_only=True)

    class Meta:
        model = Shop
        fields = [
            'id',
            'name',
            'descriptions',
            'image',
            'parent_category',
            'child_category',
            'date_add',
            'owner',
            'parent_category_name',
            'child_category_name',
            'country'
        ]


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Client
        fields = ('__all__')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ClientSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ClientSerializer, self).update(instance, validated_data)




