# Generated by Django 5.0.4 on 2024-05-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird')], default='Dog', max_length=100),
        ),
    ]
