from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from djmoney.models.fields import MoneyField


class MainCatalog(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва головного каталогу')

    class Meta:
        verbose_name = 'Головний каталог'
        verbose_name_plural = 'Головні каталоги'

    def __str__(self):
        return self.name


class Catalog(models.Model):
    mainCatalog = models.ForeignKey(MainCatalog, on_delete=models.CASCADE, verbose_name='Назва головного каталогу',
                                    related_name='MainCatalogRel')
    name = models.CharField(max_length=30, verbose_name='Назва підкаталогу')

    class Meta:
        verbose_name = 'Підкаталог'
        verbose_name_plural = 'Підкаталоги'

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Назва товару')
    price = MoneyField(max_digits=9, decimal_places=2, default_currency='UAH', verbose_name='Ціна')
    details = models.CharField(max_length=99, verbose_name='Характеристики')
    catalog = models.ForeignKey(Catalog, null=True, blank=True, default='', on_delete=models.CASCADE,
                                verbose_name='catalog', related_name='CatalogRel')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    image = models.ImageField(verbose_name='Фото')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товар',
                              related_name='imageRel')

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def __str__(self):
        return 'Зображення'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    date = models.DateTimeField(verbose_name='Дата створення')
    goods = models.ManyToManyField(Goods)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def get_count_goods(self):
        return Order.objects.count()

    def get_goods(self):
        return "\n".join([g.name for g in self.goods.all()])


class Comment(models.Model):
    text = models.CharField(max_length=199, verbose_name='Текст коментарія')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, verbose_name='Користувач')

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
