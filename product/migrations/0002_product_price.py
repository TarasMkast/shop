# Generated by Django 3.1 on 2020-08-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=1, verbose_name='Ціна'),
        ),
    ]
