from django.db import models
from product.models import Product


class Order(models.Model):
    email = models.EmailField(verbose_name='Електронна пошта')
    first_name = models.CharField(max_length=50, verbose_name='Імя')
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    city = models.CharField(max_length=100, verbose_name='Місто')
    address = models.CharField(max_length=250, verbose_name='Адреса')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    paid = models.BooleanField(default=False, verbose_name='Оплата')

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def get_count_goods(self):
        return Order.objects.count()

    def __str__(self):
        return self.first_name.join(' ').join(self.last_name)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Замовив(ла)')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.FloatField(default=0, verbose_name='Ціна')
    quantity = models.IntegerField(default=1, verbose_name='Кількість')

    class Meta:
        verbose_name = 'Замовлений товар'
        verbose_name_plural = 'Замовлені товари'
