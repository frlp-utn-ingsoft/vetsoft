# Generated by Django 5.0.4 on 2024-05-03 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_provider_product_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.provider'),
        ),
    ]
