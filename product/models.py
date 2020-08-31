from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models
from djmoney.forms import MoneyField
from mainsite.models import Catalog


class Product(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Назва товару')
    price = models.FloatField(default=1, verbose_name='Ціна')
    details = models.CharField(max_length=99, verbose_name='Характеристики')
    catalog = models.ForeignKey(Catalog, null=True, blank=True, default='', on_delete=models.CASCADE,
                                verbose_name='catalog', related_name='CatalogRel')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class PropertyImage(models.Model):
    image_caption = models.CharField(max_length=35)
    image = models.ImageField(verbose_name='Зображення')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар',
                                related_name='imageRel')

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.image_caption
