# Generated by Django 3.2.5 on 2021-07-13 06:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('child_category', models.ManyToManyField(to='shop.ChildCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('wholesale_price', models.DecimalField(decimal_places=2, help_text='Оптовая цена', max_digits=12)),
                ('weight', models.FloatField(help_text='Вес', max_length=12)),
                ('weight_choices', models.CharField(choices=[('KG', 'Кг'), ('GR', 'Гр')], default='KG', max_length=12)),
                ('sale', models.IntegerField(blank=True, help_text='Скидка', null=True)),
                ('dae_add', models.DateField(auto_now=True)),
                ('child_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.childcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('child_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.childcategory')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.parentcategory')),
                ('products', models.ManyToManyField(to='shop.Products')),
            ],
        ),
        migrations.CreateModel(
            name='ShopUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('user_choices', models.CharField(choices=[('SELLER', 'Продавец'), ('BUYER', 'Покупатель')], default='BUYER', max_length=255)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ManyToManyField(to='shop.ProductsImage'),
        ),
        migrations.AddField(
            model_name='products',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.parentcategory'),
        ),
    ]
