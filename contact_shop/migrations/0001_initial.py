# Generated by Django 3.1 on 2020-08-17 14:01

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Електронний адрес')),
                ('number_tel', phone_field.models.PhoneField(max_length=13, verbose_name='Номер телефону')),
                ('address', models.CharField(max_length=30, verbose_name='Адреса')),
            ],
            options={
                'verbose_name': 'Контактна інформація',
                'verbose_name_plural': 'Контактна інформація',
            },
        ),
    ]
