# Generated by Django 3.2.12 on 2022-03-01 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20220301_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRDISactive',
        ),
    ]
