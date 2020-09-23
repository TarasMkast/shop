# Generated by Django 3.1 on 2020-09-21 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_main', models.ImageField(upload_to='', verbose_name='Зображення')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Назва товару')),
                ('price', models.FloatField(default=1, verbose_name='Ціна')),
                ('details', models.CharField(max_length=99, verbose_name='Характеристики')),
                ('catalog', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CatalogRel', to='mainsite.catalog', verbose_name='catalog')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_caption', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to='', verbose_name='Зображення')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageRel', to='product.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Зображення',
                'verbose_name_plural': 'Зображення',
            },
        ),
    ]
