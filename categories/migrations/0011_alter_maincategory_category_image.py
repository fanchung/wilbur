# Generated by Django 3.2.12 on 2022-02-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_auto_20220216_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/main/imgs/', verbose_name='Category Image'),
        ),
    ]
