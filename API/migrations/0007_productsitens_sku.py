# Generated by Django 3.1.2 on 2020-12-29 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20201229_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsitens',
            name='SKU',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
