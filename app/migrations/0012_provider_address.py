# Generated by Django 5.0.4 on 2024-05-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_pet_vets'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
