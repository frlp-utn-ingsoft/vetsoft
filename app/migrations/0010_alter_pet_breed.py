# Generated by Django 5.0.4 on 2024-05-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_merge_0008_alter_pet_breed_0008_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Conejo', 'Conejo'), ('Pájaro', 'Pájaro'), ('Pez', 'Pez'), ('Otro', 'Otro')], max_length=50),
        ),
    ]
