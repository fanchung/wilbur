# Generated by Django 3.2.12 on 2022-02-04 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='products/imgs/<django.db.models.fields.related.ForeignKey>/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product')),
            ],
        ),
    ]
