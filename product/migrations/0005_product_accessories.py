# Generated by Django 3.1.7 on 2021-03-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210314_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternatives', models.ManyToManyField(related_name='accessories_products', to='product.Product', verbose_name='Accessories')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_prodcut', to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Accessory',
                'verbose_name_plural': 'Product Accessories',
            },
        ),
    ]
