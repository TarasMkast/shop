from django.contrib.auth.models import User
from django.db import models


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
