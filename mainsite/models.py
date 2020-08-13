from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from djmoney.models.fields import MoneyField


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Користувач')
    date = models.DateTimeField(verbose_name='Дата створення')

    def count_goods(self):
        return Goods.objects.annotate(Count('order'))

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class Goods(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Назва товару')
    price = MoneyField(max_digits=9, decimal_places=2, default_currency='UAH', verbose_name='Ціна')
    details = models.CharField(max_length=99, verbose_name='Характеристики')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders', verbose_name='замовлення')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class PropertyImage(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField(verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class MainCatalog(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва головного каталогу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Головний каталог'
        verbose_name_plural = 'Головні каталоги'


class Catalog(models.Model):
    mainCatalog = models.ForeignKey(MainCatalog, on_delete=models.CASCADE, verbose_name='Назва головного каталогу')
    name = models.CharField(max_length=30, verbose_name='Назват підкаталогу')

    class Meta:
        verbose_name = 'Підкаталог'
        verbose_name_plural = 'Підкаталоги'


class Comment(models.Model):
    text = models.CharField(max_length=199, verbose_name='Текст коментарія')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, verbose_name='Користувач')

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
