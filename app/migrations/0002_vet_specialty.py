# Generated by Django 5.0.4 on 2024-05-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vet',
            name='specialty',
            field=models.CharField(choices=[('Sin especialidad', 'Sin Especialidad'), ('Cardiología', 'Cardiologia'), ('Medicina interna de pequeños animales', 'Medicina Interna Pequenos Animales'), ('Medicina interna de grandes animales', 'Medicina Interna Grandes Animales'), ('Neurología', 'Neurologia'), ('Oncología', 'Oncologia'), ('Nutrición', 'Nutricion')], default='Sin especialidad', max_length=100),
        ),
    ]