# Generated by Django 4.1.3 on 2022-11-19 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imagesAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='original_url',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ImageUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagesAPI.accounttier')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
