# Generated by Django 3.0.1 on 2020-04-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facts', '0004_auto_20200421_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]