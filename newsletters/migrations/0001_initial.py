# Generated by Django 3.1.2 on 2022-05-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('email_date', models.DateTimeField(auto_now_add=True)),
                ('subscribed', models.BooleanField(default=False, verbose_name='Subscribed')),
            ],
            options={
                'verbose_name': 'News letter',
                'verbose_name_plural': 'News letters',
                'ordering': ('-email_date',),
            },
        ),
    ]