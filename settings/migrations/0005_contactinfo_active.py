# Generated by Django 3.1.2 on 2022-05-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20220506_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
