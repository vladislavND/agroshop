from django.db import models
from django.contrib.auth.models import User


class ChildCategory(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class ParentCategory(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    child_category = models.ManyToManyField(ChildCategory)

    def __str__(self):
        return f'{self.name}'


class ProductsImage(models.Model):
    image = models.ImageField(upload_to='shop/images')

    # TODO: Доделать метод сохранения изображений в определенную директорию
    def directory_image(self, username, shop_name):
        image = self.image


class Products(models.Model):
    KG = 'KG'
    GR = 'GR'
    WEIGHT_CHOICES = [
        (KG, 'Кг'),
        (GR, 'Гр')
    ]
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=12, decimal_places=2, help_text='Оптовая цена')
    weight = models.FloatField(max_length=12, help_text='Вес')
    weight_choices = models.CharField(max_length=12, choices=WEIGHT_CHOICES, default=KG)
    sale = models.IntegerField(null=True, blank=True, help_text='Скидка')
    bargain_bool = models.BooleanField(default=False, help_text='Торг')
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    child_category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    image = models.ManyToManyField(ProductsImage)
    date_add = models.DateField(auto_now=True)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True, related_name='user_id')

    def __str__(self):
        return f'{self.name} Цена: {self.price}'


class Shop(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField()
    products = models.ManyToManyField(Products, related_name='products_id')
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    child_category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE, null=True, blank=True)
    date_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Users(User):
    is_seller = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)






