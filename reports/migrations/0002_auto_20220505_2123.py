# Generated by Django 3.1.2 on 2022-05-05 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportuser',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='ReportUser',
        ),
    ]
