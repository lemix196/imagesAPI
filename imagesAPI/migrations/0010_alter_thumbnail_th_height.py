# Generated by Django 4.1.3 on 2022-11-24 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesAPI', '0009_alter_image_thumbnail_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='th_height',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)]),
        ),
    ]
