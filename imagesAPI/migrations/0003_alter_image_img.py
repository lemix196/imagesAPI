# Generated by Django 4.1.3 on 2022-11-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesAPI', '0002_image_original_url_imageuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]