# Generated by Django 2.2.5 on 2019-12-19 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191130_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='oussema',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]