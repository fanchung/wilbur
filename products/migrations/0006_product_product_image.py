# Generated by Django 3.2.12 on 2022-02-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_prdslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='products/imgs/', verbose_name='Product Image'),
            preserve_default=False,
        ),
    ]
