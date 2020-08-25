# Generated by Django 3.1 on 2020-08-25 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20200825_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Замовлений товар', 'verbose_name_plural': 'Замовлені товари'},
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.goods', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.order', verbose_name='Замовив(ла)'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.FloatField(default=0, verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Кількість'),
        ),
    ]