# Generated by Django 3.1.7 on 2021-03-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210316_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSLug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]