# Generated by Django 3.2.12 on 2022-02-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0017_auto_20220217_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='category_image',
            field=models.ImageField(blank=True, help_text='Please use our recommended dimensions: 120px X 120px', null=True, upload_to='categories/main/imgs/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='minicategory',
            name='category_image',
            field=models.ImageField(blank=True, help_text='Please use our recommended dimensions: 120px X 120px', null=True, upload_to='categories/mini/imgs/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category_image',
            field=models.ImageField(blank=True, help_text='Please use our recommended dimensions: 120px X 120px', null=True, upload_to='categories/sub/imgs/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='supercategory',
            name='category_image',
            field=models.ImageField(blank=True, help_text='Please use our recommended dimensions: 120px X 120px', null=True, upload_to='categories/super/imgs/', verbose_name='Category Image'),
        ),
    ]
