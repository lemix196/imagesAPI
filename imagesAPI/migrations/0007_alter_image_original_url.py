# Generated by Django 4.1.3 on 2022-11-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesAPI', '0006_alter_image_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='original_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
