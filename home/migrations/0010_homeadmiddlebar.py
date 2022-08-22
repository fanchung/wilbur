# Generated by Django 3.2.12 on 2022-02-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_homead_homeadsidebar'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAdMiddlebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_mage', models.ImageField(blank=True, help_text='Please use our recommended dimensions: 768px x 450px, 250 KB MAX', null=True, upload_to='ads/', verbose_name='Image')),
                ('ad_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('ad_URL', models.URLField(blank=True, null=True)),
                ('image_position', models.CharField(choices=[('Right', 'Right')], default='Right', max_length=13)),
            ],
        ),
    ]
