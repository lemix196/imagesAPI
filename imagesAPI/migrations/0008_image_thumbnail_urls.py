# Generated by Django 4.1.3 on 2022-11-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesAPI', '0007_alter_image_original_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail_urls',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
