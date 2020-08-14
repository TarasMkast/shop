from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    email = models.EmailField(verbose_name='Електронний адрес')
    number_tel = PhoneField(max_length=13, verbose_name='Номер телефону')
    address = models.CharField(max_length=30, verbose_name='Адреса')

    class Meta:
        verbose_name = 'Контактна інформація'
        verbose_name_plural = 'Контактна інформація'
