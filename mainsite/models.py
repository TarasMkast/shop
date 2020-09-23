from django.contrib.auth.models import User
from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=30, verbose_name='Каталог')
    parent_id = models.ForeignKey('Catalog', null=True, blank=True, on_delete=models.CASCADE,
                                  verbose_name='Батьківський каталог')

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name
