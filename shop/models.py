from django.db import models
from django.contrib.auth.models import User


class Village(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True, related_name='citys')
    big_city = models.BooleanField(default=False, help_text='Город областного значения')


class Region(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name='regions')


class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name='countries')


class ChildCategory(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class ParentCategory(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    child_category = models.ManyToManyField(ChildCategory)

    class Meta:
        verbose_name = 'Родительская категория'
        verbose_name_plural = 'Родительские категории'

    def __str__(self):
        return f'{self.name}'


class ProductsImage(models.Model):
    image = models.ImageField(upload_to='shop/images/products')

    # TODO: Доделать метод сохранения изображений в определенную директорию
    def directory_image(self, username, shop_name):
        image = self.image


class Client(User):
    is_seller = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.username}'


class Product(models.Model):
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
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='products')
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    date_add = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Цена: {self.price}'

    def products_sale_price(self):
        if self.sale:
            """Получаем цену со скидкой"""
            count = self.price / 100 * self.sale
            return self.price - count


class Shop(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='shop/images/shops')
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    child_category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE, null=True, blank=True)
    date_add = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='shops')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name='shops')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f'{self.name}'






