# Generated by Django 3.2.12 on 2022-03-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_remove_product_prdisactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDISactive',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
